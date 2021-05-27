from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
# MVC Framework
# Model View Controller

def index(request):
    return HttpResponse("Hello, this app seems to be working fine.")
