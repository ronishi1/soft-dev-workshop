# Ray Onishi
# SoftDev1 pd7
# K26 -- Getting More REST
# 2018-11-15

import json
import urllib
import random

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # REST Countries API
    u = urllib.request.urlopen("https://restcountries.eu/rest/v2/region/europe")
    #print (u)
    request = u.read()
    #print (request)
    countryData = json.loads(request)
    #print(countryData)

    randCountry = random.choice(countryData)
    lat = randCountry['latlng'][0]
    lng = randCountry['latlng'][1]

    # Sunset and Sunrise API
    url = "https://api.sunrise-sunset.org/json?lat={}&lng={}"
    u = urllib.request.urlopen(url.format(lat,lng))
    request = u.read()
    randSunData = json.loads(request)
    randCountry['sunData'] = randSunData

    # Dog API
    u = urllib.request.urlopen("https://dog.ceo/api/breeds/image/random")
    request = u.read()
    dogData = json.loads(request)

    return render_template('home.html',countries=countryData,rCountry = randCountry,dog=dogData)

if __name__ == "__main__":
    app.debug = True
    app.run()
