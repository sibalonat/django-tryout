from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request) :
    return HttpResponse('Hello, world')

def marin(request) :
    return HttpResponse('Hello, world')

def fry(request, name) :
    return HttpResponse(f'Hello, {name}')
