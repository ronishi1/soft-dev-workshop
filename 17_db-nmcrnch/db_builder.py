# Small Elephants: Maggie Zhao & Qian Zhou
# SoftDev1 pd7
# K16-- No Trouble
# 2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

#==========================================================

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE


#building peeps table
command = "CREATE TABLE peeps(name TEXT, age INTEGER, id INTEGER)"

#build SQL stmt, save as string
c.execute(command)    #run SQL statement
with open('peeps.csv') as csvfile:
    readerPeeps = csv.DictReader(csvfile)
    for row in readerPeeps:
        # '?' is used as a placeholder for values. provide a tuple of values as the second argument to the execute() method
        # from the sqlite documentation: You shouldn't assemble your query using Python's string operations because doing so is insecure; it makes your program vulnerable to an SQL injection attack
        command = "INSERT INTO peeps (name, age, id)VALUES (?,?,?)"
        values = [(row["name"], row["age"], row["id"])]
        # executemany(SQL, [parameters]) where parameters is a list of tuples
        c.executemany(command, values)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#building courses table
command = "CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)"

#build SQL stmt, save as string
c.execute(command)

with open('courses.csv') as csvfile:
    readerCourses = csv.DictReader(csvfile)
    for row in readerCourses:
        command = "INSERT INTO courses (code, mark, id)VALUES (?,?,?)"
        values = [(row["code"], row["mark"], row["id"])]

        c.executemany(command, values)


#==========================================================

db.commit() #save changes
db.close()  #close database
