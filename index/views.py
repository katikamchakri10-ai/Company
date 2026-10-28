from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import about1
from.models import ourteam
from.models import client
from.models import article
from.models import price
from.models import contactforms
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.conf import settings
from google import genai
from google.genai.errors import ServerError
from pathlib import Path
from pypdf import PdfReader
import os
import time
def home(request):
    aboutdata=about1.objects.all()[0]
    clientdata=client.objects.all()
    
    context={
        'about1':aboutdata,
        'client':clientdata,
        
    }
    return render(request,'index.html',context)

def about(request):
    ourteamdata=ourteam.objects.all()
    clientdata=client.objects.all()
    context={
        'ourteam':ourteamdata,
        'client':clientdata
    }
    return render(request,'about.html',context)

def services(request):
    return render(request,'services.html')

def portfolio(request):
    
    return render(request,'portfolio.html')

def pricing(request):
    pricingdata=price.objects.all()[0]
    context={
        'price':pricingdata,
    }
    return render(request,'pricing.html',context)

def blog(request):
    articledata=article.objects.all()
    context={
        'article':articledata
    }

    return render(request,'blog.html',context)

def contact(request):
    print("CONTACT VIEW FILE:", __file__)

    if request.method=="POST":
        name=request.POST.get("name","").strip()
        email=request.POST.get("email","").strip()
        subject=request.POST.get("subject","").strip()
        message_text=request.POST.get("message","").strip()

        if name and email and subject and message_text:
            contactforms.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message_text,
            )
            messages.success(
                request,
                "Thank you!, your message has been submitted"
                )
            return redirect("/#contact")
        messages.error(
            request,
            "please fill in all contact form fields."
            )
    return render(request,'contact.html')

def servicedetails(request):
    return render(request,'service-details.html')
def team(request):
    return render(request,'team.html')

def testimonials(request):
    return render(request,'testimonials.html')


@require_POST
def chatbot_api(request):

    # Get the customer's question
    question = request.POST.get("message", "").strip()

    if not question:
        return JsonResponse(
            {"error": "Please enter a question."},
            status=400
        )

    if len(question) > 1000:
        return JsonResponse(
            {
                "error": "Please keep your question under 1000 characters."
            },
            status=400
        )

    # Get Gemini API key
    api_key = os.environ.get("GOOGLE_API_KEY")

    if not api_key:
        return JsonResponse(
            {
                "error": "AI API key is not configured on the server."
            },
            status=500
        )

    try:
        # Find the PDF in the knowledge folder
        pdf_path = (
            Path(settings.BASE_DIR)
            / "knowledge"
            / "website_overview_knowledge_base.pdf"
        )

        # Check whether the PDF exists
        if not pdf_path.exists():
            print("PDF NOT FOUND:", pdf_path)

            return JsonResponse(
                {
                    "error": (
                        "website overview knowledge base PDF was not found. "
                        "Please check the knowledge folder."
                    )
                },
                status=500
            )

        # Read text from the PDF
        reader = PdfReader(str(pdf_path))
        website_info = []

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                website_info.append(page_text)

        context = "\n".join(website_info)

        if not context.strip():
            return JsonResponse(
                {
                    "error": (
                        "No readable text was found in the PDF."
                    )
                },
                status=500
            )

        # Connect to Gemini
        client = genai.Client(api_key=api_key)

        # Retry temporary Gemini server errors up to 3 times
        for attempt in range(3):

            try:
                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=(
                        "You are a helpful customer support assistant "
                        "for the Company website.\n\n"

                        "Use the supplied PDF as your knowledge base.\n"
                        "Answer questions about products, prices, "
                        "monthly deals and website services using "
                        "only information supported by the PDF.\n"
                        "Do not invent product names, prices, stock "
                        "availability, delivery details or offers.\n"
                        "If the information is missing from the PDF, "
                        "say that you cannot confirm it from the "
                        "available information.\n\n"

                        f"website_overview_knowledge_base PDF INFORMATION:\n{context}\n\n"
                        f"CUSTOMER QUESTION:\n{question}"
                    )
                )

                answer = response.text

                if not answer:
                    return JsonResponse(
                        {
                            "error": (
                                "The AI returned an empty response. "
                                "Please try again."
                            )
                        },
                        status=503
                    )

                return JsonResponse({
                    "answer": answer
                })

            except ServerError:
                if attempt == 2:
                    raise

                # Wait before retrying
                time.sleep(3)

    except Exception as e:
        import traceback

        traceback.print_exc()
        print("GEMINI CHATBOT ERROR:", repr(e))

        return JsonResponse(
            {
                "error": (
                    "Sorry, the AI assistant is temporarily busy "
                    "or the knowledge PDF could not be processed. "
                    "Please try again later."
                )
            },
            status=503
        )