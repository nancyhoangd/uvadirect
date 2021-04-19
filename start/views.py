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
        dayInfo = parseWeatherResponse(api_response_json)
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
                "img": getImgURL("--")
            }
        }
        for i in range(6):
            dayInfo["day"+str(i+1)] = {
                "day": "-- -- ----",
                "F": "--",
                "C": "--",
                "sky": "--",
                "desc": "--",
                "img": getImgURL("--")
            }
    return dayInfo

    
        

def parseWeatherResponse(api_response_json):
    today = api_response_json["daily"][0]
    date = dtToDate(today["dt"], True)
    todayInfo = {
        "weekday" : date[0],
        "date": date[1],
        "F": round((today["temp"]["day"]-273.15)*9/5+32),
        "C": round((today["temp"]["day"]-273.15)),
        "min": round((today["temp"]["min"]-273.15)*9/5+32),
        "max": round((today["temp"]["max"]-273.15)*9/5+32),
        "sky": today["weather"][0]["main"],
        "desc": today["weather"][0]["description"],
        "img": getImgURL(today["weather"][0]["description"])
    }
    print(todayInfo["img"])
    days=[]
    for i in range(6):
        nextDay = api_response_json["daily"][i+1]
        date = dtToDate(nextDay["dt"])
        days.append({
            "weekday" : date[0],
            "date": date[1],
            "max": round((nextDay["temp"]["max"]-273.15)*9/5+32),
            "min": round((nextDay["temp"]["min"]-273.15)*9/5+32),
            "sky": nextDay["weather"][0]["main"],
            "desc": nextDay["weather"][0]["description"],
            "img": getImgURL(nextDay["weather"][0]["description"])
        })
    hours=[]
    for i in range(6):
        hour = api_response_json["hourly"][i+1]
        hours.append({
            "time" : datetime.utcfromtimestamp(int(hour["dt"])-4*3600).strftime('%I:%M%p').strip("0"),
            "temp" : round((hour["temp"]-273.15)*9/5+32),
            "desc" : hour["weather"][0]["description"],
            "img": getImgURL(hour["weather"][0]["description"])
        })
    return { "today" : todayInfo, "days" : days, "hours" : hours }

def dtToDate(dt, includeYear=False):
    dt = int(dt)-4*3600
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
    info = datetime.utcfromtimestamp(int(dt)).strftime('%m %d %Y %A').split(" ")
    month = months[int(info[0])]
    day = "st"
    if(info[1][-1] == "2" and info[1] != "12"):
        day = "nd"
    elif(info[1][-1] == "3" and info[1] != "13"):
        day = "rd"
    elif(info[1][-1] != "1" or info[1] == "11"):
        day = "th"
    if(int(info[1]) < 10):
        info[1] = info[1][-1]
    if(includeYear):
        info[2] = ", " + info[2]
    else:
        info[2] = ""
    print(info)
    return (info[3], month + " " + info[1]+day + info[2])

def getImgURL(weatherDescription):
    prefix = ""#"{% static \'assets/img/weatherIcons/"
    suffix = ""#"\' %}"
    if(weatherDescription == "--"):
        return prefix + "unknown.jpg" + suffix
    elif(weatherDescription == "clear sky"):
        return prefix + "sunny.jpg" + suffix
    elif(weatherDescription == "overcast clouds"):
        return prefix + "overcast.jpg" + suffix
    elif(weatherDescription == "light rain"):
        return prefix + "light_rain.jpg" + suffix
    elif(weatherDescription == "moderate rain"):
        return prefix + "rainy.jpg" + suffix
    elif(weatherDescription == "few clouds" or weatherDescription == "scattered clouds" or weatherDescription == "broken clouds"):
        return prefix + "partly_cloudy.jpg" + suffix
    elif(weatherDescription == "heavy intensity rain"):
        return prefix + "heavy_rain.jpg" + suffix
def home(request):
    return HttpResponse("Hello, world. You're at the Grounds Map Start home.")

