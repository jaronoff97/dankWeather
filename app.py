from flask import Flask, render_template
from math import log
import requests
import json
import os

app = Flask(__name__)
forecastAPIKey = os.environ.get('FORECAST_IO_API_KEY')


@app.route('/')
def home():
    response = requests.get(
        "https://api.forecast.io/forecast/{0}/42.360082,-71.058880".format(forecastAPIKey))
    data = json.loads(response.text)
    latitude = data["latitude"]
    longitude = data["longitude"]
    temp = data["currently"]["temperature"]
    humid = data["currently"]["humidity"]
    wind = data["currently"]["windSpeed"]
    rain = data["currently"]["precipIntensity"]

    dank = str(int(dankCalc(temp, humid, wind, rain))) + "%"
    return render_template('index.html', info_location=dank), 200


def dankCalc(temp, humid, wind, rain):
    temp = dankTemp(temp)
    humid = dankHumid(humid)
    wind = dankWind(wind)
    rain = dankRain(rain)

    return (temp * humid * wind * rain) * 100


def dankTemp(temp):
    if temp > 40 or temp <= 100:
        return (100 - abs(70 - temp) ** 1.354)/100
    else:
        return 0


def dankHumid(humid):
    if humid < .5:
        return (100 - 100 * abs(.25 - humid) ** ((log(2, 10) + log(5, 10)) / log(5, 10)))/100
    else:
        return 0


def dankWind(wind):
    if wind < 26.5:
        return (100 - abs(5 - wind) ** 1.5)/100
    else:
        return 0


def dankRain(rain):
    if rain < .1:
        return (100 - rain * 1000)/100
    else:
        return 0

if __name__ == '__main__':  # only run if this is being run as the main app
    context = ('chained.pem', 'domain.key')
    app.run(host='0.0.0.0', ssl_context=context, port=443)
