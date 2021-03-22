from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def map_page(request):
    return HttpResponse("Maps display page")
