#Ray Onishi & Amit Narang - Snakes
#SoftDev1 pd7
#K16 -- No trouble
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

db = sqlite3.connect("discobandit.db")
c = db.cursor()

peeps = {"name":"TEXT","age":"INTEGER","id":"INTEGER"}
occupations = {"Job Class":"TEXT","Percentage":"INTEGER"}
courses = {"code":"TEXT","mark":"INTEGER","id":"INTEGER"}

def buildTable(file,headers,tableName):
    headerInfo = ""
    for key in headers:
        headerInfo += key + " " + headers[key] + ","
    headerInfo = headerInfo[:-1]
    print(headerInfo)
    c.execute("CREATE TABLE " + tableName + "(" + headerInfo + ")")
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cmd = "("
            for key in headers:
                if headers[key] == "TEXT":
                    cmd += "\"" + row[key] + "\","
                else:
                    cmd += row[key] + ","
            cmd = cmd[:-1]
            cmd += ")"
            c.execute("INSERT INTO " + tableName + " VALUES" + cmd)

buildTable('peeps.csv',peeps,"peeps")
buildTable('occupations.csv',occupations,"occupations")
buildTable('courses.csv',courses,"courses")

db.commit() #save changes
db.close()  #close database
