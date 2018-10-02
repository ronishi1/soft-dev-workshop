# Ray Onishi, Shafali Gupta - Devo Squad!
# SoftDev1 pd7
# K14 -- Do I Know You?
# 2018-10-01

from flask import Flask,render_template,session,request,url_for,redirect
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

user1 = "tester"
pass1 = "test"

error = ""

def check_credentials(username,password):
    return username == user1 and password == pass1

@app.route("/")
def home():
    if "user" in session:
        return render_template('auth.html',username=session["user"])
    return render_template('login.html',errorMessage=error)

@app.route("/logout")
def logout():
    session.pop("user")
    return redirect(url_for('home'))

@app.route("/auth",methods=["POST"])
def authenticate():
    global error
    username = request.form['username']
    password = request.form['password']
    if check_credentials(username,password):
        session["user"] = username
    elif username != user1:
        error = "bad username!"
    else:
        error = "bad password!"
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.debug = True
    app.run()
