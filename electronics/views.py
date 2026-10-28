from django.shortcuts import render
from django.http import HttpResponse

def electronics(request):
    return HttpResponse('This is electronics page')

def laptop(request):
    return HttpResponse('This is laptop page')

def tv(request):
    return HttpResponse('This is tv page')

def fridge(request):
    return HttpResponse('This is fridge page')

def ac(request):
    return HttpResponse('This is ac page')
