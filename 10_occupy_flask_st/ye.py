#Peter Cwalina, Ray Onishi - sCwishi Jinjas
#SofDev1 pd 7
#K10 -- Jinja Tuning
#2018-09-22

# importing what is needed to read the csv and choose a random occupation

from util import csvStuff
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return '<a href="/occupations">To the homework</a>'

@app.route("/occupations")
def occRoute():
    occDict = csvStuff.makeDict('data/occupations.csv') #creates the dictionary of occupations
    return render_template('occ.html',#rendering the template with set params
                           title ='Occupation Data',
                           heading = 'Here\'s some cool data on occupation percentages',
                           occ = csvStuff.randomKey(occDict), #sets the variable occ to a random occupation
                           dict = occDict
    )

if __name__ == "__main__" :
    app.debug = True
    app.run()
