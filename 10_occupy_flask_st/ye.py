#Peter Cwalina, Ray Onishi - sCwishi Jinjas
#SofDev1 pd 7
#K10 -- Jinja Tuning
#2018-09-22

# importing what is needed to read the csv and choose a random occupation
import csv, random

from flask import Flask, render_template
app = Flask(__name__)
#function for returning a random key based on the weights in the dict
def randomKey(dict):
    keys = []
    for key in dict:
        if key != 'Job Class':#job class and total arent to be chosen from
            if key != 'Total':
                keys = keys + [key] * int(dict[key] * 10)
    return random.choice(keys)



@app.route("/occupations")
def occRoute():
    # creates a dictionary out of occupations.csv
    occDict = {}
    with open('data/occupations.csv') as file:
        csvReader = csv.reader(file, delimiter = ',')
        for row in csvReader:
            if row[0] != "Job Class":#just to make sure we dont accidentally turn a string into a float
                occDict[row[0]] = float(row[1])
            else:
                occDict[row[0]] = row[1]


    return render_template('occ.html',#rendering the template with set params
                           title ='Occupation Data',
                           heading = 'Here\'s some cool data on occupation percentages',
                           occ = randomKey(occDict),
                           dict = occDict
    )

if __name__ == "__main__" :
    app.debug = True
    app.run()
