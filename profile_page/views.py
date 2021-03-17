from django.shortcuts import render
from django.http import HttpResponse


def profile(request):
    return HttpResponse("Display Profile Info Here")
def edit_info(request):
    return HttpResponse("Page to Edit Profile Info")
def privacy(request):
    return HttpResponse("Privacy Settings")
def schedule(request):
    return HttpResponse("Schedule building page")