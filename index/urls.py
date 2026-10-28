
from django.urls import path,include
from . import views

urlpatterns =[
    
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('pricing/',views.pricing,name='pricing'),
    path('blog/',views.blog,name='blog'),
    path('contact/',views.contact,name='contact'),
    path('servicedetails/',views.servicedetails,name='servicedetails'),
    path('team/',views.team,name='team'),
    path('testimonials/',views.testimonials,name='testimonials'),
    path('chatbot-api/', views.chatbot_api, name='chatbot_api'),

]
