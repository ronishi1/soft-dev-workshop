# Ray Onishi
# SoftDev1 pd7
# K24 -- A RESTful Journey Skyward
# 2018-11-13

from flask import Flask, render_template
import json
import urllib

app = Flask(__name__)

@app.route("/")
def home():
    request = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=F47oFEQYOK5d7ipZuL5uNCCSTydf8GjMuwyGttmA&date=2017-05-14")
    #print (request)

    data = request.read()
    #print (data)

    dataDict = json.loads(data)
    #print(dataDict)

    return render_template('nasa.html',pic=dataDict['url'],explanation=dataDict['explanation'])

if __name__ == "__main__":
    app.debug = True
    app.run()
