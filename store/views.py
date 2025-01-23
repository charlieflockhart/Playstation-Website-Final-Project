from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def my_store(request):
    return HttpResponse("Hello, Playstation!")