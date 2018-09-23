#Peter Cwalina, Ray Onishi - sCwishi Jinjas
#SofDev1 pd 7
#K10 -- Jinja Tuning
#2018-09-22

# importing what is needed to read the csv and choose a random occupation
import csv, random

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/occupations")
def occRoute():
    # creates a dictionary out of occupations.csv
    occDict = {}
    with open('data/occupations.csv') as file:
        csvReader = csv.reader(file, delimiter = ',')
        for row in csvReader:
            if row[0] != "Job Class":
                occDict[row[0]] = float(row[1])
            else:
                occDict[row[0]] = row[1]


    # selects a random occupation
    occupation = []
    for key in occDict:
        if key != 'Job Class':
            if key != 'Total':
                occupation = occupation + [key] * int(occDict[key] * 10)
    ranOcc = random.choice(occupation)

    # testing the ranOcc
    # print(ranOcc)

    return render_template('occ.html',
                           title ='Occupation Data',
                           heading = 'Here\'s some cool data on occupation percentages',
                           occ = ranOcc,
                           dict = occDict
    )

if __name__ == "__main__" :
    app.debug = True
    app.run()
