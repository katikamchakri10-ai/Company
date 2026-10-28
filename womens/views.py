from django.shortcuts import render
from django.http import HttpResponse

def womens(request):
    return HttpResponse('This is womens page')

def handbags(request):
    return HttpResponse('This is handbags page')

def cosmetics(request):
    return HttpResponse('this is cosmetics page')

