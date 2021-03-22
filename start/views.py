from django.shortcuts import render
from django.http import HttpResponse

#if this doesnt work import at beg of every function
import requests
import json


def index(request):
    return HttpResponse("Hello, world. You're at the Grounds Map Start index.")

# for the weather tab
def weather(request):
    link_url = \
        "https://api.openweathermap.org/data/2.5/onecall?lat=33.441792&lon=-94.037689&exclude=minutely&appid=26d6cab8e9456aaac762ee09a57c1ca9"
    api_request = requests.get(link_url)
    api = json.loads(api_request.content)
    print(api)

weather("hi")