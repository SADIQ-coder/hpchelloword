from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.d

def homePageView(request):
    return HttpResponse('Hello World')