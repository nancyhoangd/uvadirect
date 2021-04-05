function getToday(weatherRequest)
{   
    var today = weatherRequest.daily[0]
    var todayInfo = {
        "F": (today.temp.day-273.15)*9/5+32,
        "C": (today.temp.day-273.15),
        "min": (today.temp.min-273.15)*9/5+32,
        "max": (today.temp.max-273.15)*9/5+32,
        "sky": today.weather[0].main,
        "desc": today.weather[0].description
    };
    return todayInfo
}
function getDay(weatherRequest, delta)
{   
    var today = weatherRequest.daily[delta]
    var todayInfo = {
        "F": (today.temp.day-273.15)*9/5+32,
        "C": (today.temp.day-273.15),
        "min": (today.temp.min-273.15)*9/5+32,
        "max": (today.temp.max-273.15)*9/5+32,
        "sky": today.weather[0].main
    };
    return todayInfo
}