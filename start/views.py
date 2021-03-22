from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, world. You're at the Grounds Map Start home.")


def weather(request):
    return HttpResponse("Weather Page")