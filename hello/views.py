from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello, This is STY Webapp hosted on Azure updated")
