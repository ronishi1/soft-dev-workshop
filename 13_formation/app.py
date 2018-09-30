# Ray Onishi
# SoftDev1 pd7
# K08 -- Echo Echo Echo
# 2018-09-28

from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('form.html')

@app.route("/auth",methods=["POST","GET"])
def auth():
    method = request.method
    if method=="GET":
        username = request.args['username']
    else:
        username = request.form['username']
    return render_template('auth.html',
                            username = username,
                            method = method)

if __name__ == "__main__":
    app.debug = True
    app.run()
