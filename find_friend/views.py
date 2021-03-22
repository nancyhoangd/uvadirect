from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def find_friend(request):
    return HttpResponse("Find Friends Page")
