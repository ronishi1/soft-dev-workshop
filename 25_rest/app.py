# Ray Onishi
# SoftDev1 pd7
# K25 -- Getting more REST
# 2018-11-14

import json
import urllib

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    numFilms = 5
    u = urllib.request.urlopen("https://ghibliapi.herokuapp.com/films?limit=" + str(numFilms))
    #print (u)

    request = u.read()
    #print (request)

    data = json.loads(request)
    #print(data)

    return render_template('home.html',films=data)

if __name__ == "__main__":
    app.debug = True
    app.run()
