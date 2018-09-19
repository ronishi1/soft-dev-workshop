# Ray Onishi
# SoftDev1 pd7
# K08 -- Fill Yer Flask
# 2018-09-19

from flask import Flask
app = Flask(__name__)

link_home = '<a href="/">To home page!</a>'
link_info = '<a href="/info">To info page!</a>'
link_other = '<a href="/other">To other page!</a>'

@app.route('/')
def home():
    home = '<h1>This is the home page</h1><p>Home sweet home</p>'
    links = link_info + '<br>' + link_other
    return home + links

@app.route('/info')
def info():
    info = '<h1>This is the info page</h1><p>It has all of the info!</p>'
    links = link_home + '<br>' + link_other
    return info + links

@app.route('/other')
def other():
    other = '<h1>This is the other page</h1><p>But what could the other page contain???</p>'
    links = link_home + '<br>' + link_info
    return other + links

app.debug = True
app.run()
