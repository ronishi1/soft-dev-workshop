#Ray Onishi & Amit Narang - Snakes
#SoftDev1 pd7
#K16 -- No trouble
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

# Creates a cursor and the database
db = sqlite3.connect("discobandit.db")
c = db.cursor()

# Dictionaries of all the headers along with their type
# We pass this into the function as a parameter
# We hardcoded the headers because we weren't sure
# how to type the different columns
peeps = {"name":"TEXT","age":"INTEGER","id":"INTEGER"}
occupations = {"Job Class":"TEXT","Percentage":"INTEGER"}
courses = {"code":"TEXT","mark":"INTEGER","id":"INTEGER"}

def buildTable(file,headers,tableName):
    headerInfo = ""
    for key in headers:
        # turns the headers from a dictionary into a string
        headerInfo += key + " " + headers[key] + ","
    headerInfo = headerInfo[:-1]
    print(headerInfo)
    c.execute("CREATE TABLE " + tableName + "(" + headerInfo + ")")
    with open(file) as csvfile:
        # read the CSV File
        reader = csv.DictReader(csvfile)
        for row in reader:
            # build the command we will execute
            cmd = "("
            for key in headers:
                # The values that are of type TEXT are enclosed by quotes
                if headers[key] == "TEXT":
                    cmd += "\"" + row[key] + "\","
                # if they are of any other type (namely INTEGER in this case)
                # they are added as is
                else:
                    cmd += row[key] + ","
            cmd = cmd[:-1]
            cmd += ")"
            # execute the command
            c.execute("INSERT INTO " + tableName + " VALUES" + cmd)
#run this function on the three CSV files
buildTable('peeps.csv',peeps,"peeps")
buildTable('occupations.csv',occupations,"occupations")
buildTable('courses.csv',courses,"courses")

db.commit() #save changes
db.close()  #close database
