from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from datetime import datetime

#if this doesnt work import at beg of every function
import requests
import json

def index_view(request):
    return render(request, 'start_page.html', {'weatherInfo': weather(request)})

# for the weather tab
def weather(request):
    link_url = \
        "https://api.openweathermap.org/data/2.5/onecall?lat=33.441792&lon=-94.037689&exclude=minutely&appid=26d6cab8e9456aaac762ee09a57c1ca9"
    
    dayInfo = {}

    try:
        api_response = requests.get(link_url)
        api_response_json = json.loads(api_response.content)
        dayInfo = parseResponse(api_response_json)
    except ConnectionError:
        dayInfo = {
            "today" : {
                "day": "-- -- ----",
                "F": "--",
                "C": "--",
                "min": "--",
                "max": "--",
                "sky": "--",
                "desc": "--",
            }
        }
        for i in range(6):
            dayInfo["day"+str(i+1)] = {
                "day": "-- -- ----",
                "F": "--",
                "C": "--",
                "sky": "--",
                "desc": "--",
            }
    return dayInfo

    
        

def parseResponse(api_response_json):
    today = api_response_json["daily"][0]
    todayInfo = {
        "day": dtToDate(today["dt"], True),
        "F": round((today["temp"]["day"]-273.15)*9/5+32, 2),
        "C": round((today["temp"]["day"]-273.15), 2),
        "min": round((today["temp"]["min"]-273.15)*9/5+32, 2),
        "max": round((today["temp"]["max"]-273.15)*9/5+32, 2),
        "sky": today["weather"][0]["main"],
        "desc": today["weather"][0]["description"]
    }
    days = {
        "today" : todayInfo
    }
    for i in range(6):
        nextDay = api_response_json["daily"][i+1]
        days["day"+str(i+1)] = {
            "day": dtToDate(nextDay["dt"]),
            "F": round((nextDay["temp"]["day"]-273.15)*9/5+32, 2),
            "C": round((nextDay["temp"]["day"]-273.15), 2),
            "sky": nextDay["weather"][0]["main"],
            "desc": nextDay["weather"][0]["description"]
        }
    return days
def dtToDate(dt, includeYear=False):
    months = {
        1 : "Jan",
        2 : "Feb",
        3 : "Mar",
        4 : "Apr", 
        5 : "May", 
        6 : "Jun", 
        7 : "Jul", 
        8 : "Aug",
        9 : "Sep",
        10 : "Oct",
        11 : "Nov",
        12 : "Dec"
    }
    info = datetime.utcfromtimestamp(int(dt)).strftime('%m %d %Y').split(" ")
    month = months[int(info[0])]
    day = "st"
    if(info[1][-1] == "2" and info[1] != "12"):
        day = "nd"
    elif(info[1][-1] == "3"):
        day = "rd"
    elif(info[1][-1] != "1" or info[1] == "11"):
        day = "th"
    if(int(info[1]) < 10):
        info[1] = info[1][-1]
    if(includeYear):
        info[2] = ", " + info[2]
    else:
        info[2] = ""
    return month + " " + info[1]+day + info[2]

    
def home(request):
    return HttpResponse("Hello, world. You're at the Grounds Map Start home.")

