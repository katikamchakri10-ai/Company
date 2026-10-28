from django.shortcuts import render
from django.http import HttpResponse\

def mens(request):
    return HttpResponse('this is mens page')

def footwears(request):
    return HttpResponse('This is footwears page')

def shoes(request):
    return HttpResponse('This is shoes page')