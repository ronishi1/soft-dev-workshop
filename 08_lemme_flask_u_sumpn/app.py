from flask import Flask
app = Flask(__name__)

link_home = '<a href="/ "> To home page!</a>'
link_info = '<a href="/info"> To info page!</a>'
link_other = '<a href="/other"> To other page!</a>'

@app.route("/")
def home():
    home = "<h1>This is the home page</h1>" + "<br>" + link_info + "<br>" + link_other
    return home

@app.route("/info")
def info():
    info = "<h1>This is the info page</h1>" + "<br>" + link_home + "<br>" + link_other
    return info

@app.route("/other")
def other():
    other = "<h1>This is the other page</h1>" + "<br>" + link_home + "<br>" + link_info
    return other

app.debug = True
app.run()
