#Ray Onishi & Amit Narang - Snakes
#SoftDev1 pd7
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

db = sqlite3.connect("basicPeeps.db")
c = db.cursor()

c.execute("CREATE TABLE snakes (name TEXT, age INTEGER, id INTEGER PRIMARY KEY)")


with open('peeps.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    s = "INSERT INTO snakes VALUES("
    for row in reader:
        cpS = s
        cpS += str(row['name'])
        cpS += ","
        cpS += row['age']
        cpS += ","
        cpS += row['id']
        cpS += ")"
        c.execute(cpS)

        
db.commit() #save changes
db.close()  #close database
