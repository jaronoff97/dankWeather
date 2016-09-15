from flask import Flask, redirect
from math import log
import requests
import json
import os

app = Flask(__name__)
@app.route('/')
def home():
    return redirect("https://dankweather.com", code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
