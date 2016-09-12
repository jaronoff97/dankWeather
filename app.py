from flask import Flask
from math import log
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get("https://api.forecast.io/forecast/50d386c2f9677bf46394c4a2180a606f/42.360082,-71.058880")
    data = json.loads(response.text)
    latitude = data["latitude"]
    longitude = data["longitude"]
    temp = data["currently"]["temperature"]
    humid = data["currently"]["humidity"]
    wind = data["currently"]["windSpeed"]
    rain = data["currently"]["precipIntensity"]

    return str(round(dankCalc(temp, humid, wind, rain), 5)) + "% dank"

def dankCalc(temp, humid, wind, rain):
    temp = dankTemp(temp)
    humid = dankHumid(humid)
    wind = dankWind(wind)
    rain = dankRain(rain)

    return (temp + humid + wind + rain) / 4

def dankTemp(temp):
    if temp > 40 or temp <= 100:
        return (100 - abs(70 - temp) ** 1.354)
    else:
        return 0

def dankHumid(humid):
    if humid < .5:
        return (100 - 100 * abs(.25 - humid) ** ((log(2,10) + log(5,10)) / log(5,10)))
    else:
        return 0

def dankWind(wind):
    if wind < 26.5:
        return (100 - abs(5 - wind) ** 1.5)
    else:
        return 0

def dankRain(rain):
    if rain < .1: 
        return (100 - rain * 1000)
    else:
        return 0

if __name__ == '__main__':  # only run if this is being run as the main app
    app.run(port=8080, debug=True)
