from flask import Flask,render_template,session
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('login.html')

@app.route("/logout")
def logout():
    return "logout page"

if __name__ == "__main__":
    app.debug = True
    app.run()
