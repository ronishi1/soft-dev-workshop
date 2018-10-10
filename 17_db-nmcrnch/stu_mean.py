# Toadrunners: Maggie Zhao & Ray Onishi
# SoftDev1 pd7
# K17 -- Average
# 2018-10-05


import sqlite3  #enable control of an sqlite database
import csv      #facilitates CSV I/O

#==========================================================

#access the database created with db_builder
DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

text_factory = bytes
#==========================================================

# Look up each student's grades DONE
# Compute each student's average DONE
# Display each student's name, id, and average DONE
# Create a table of IDs and associated averages, named "peeps_avg"
# Facilitate adding rows to the courses table


# Look up the grades of a student with their id as studentid
def lookAtGrade(studentid):
    studentinfo = {}
    key = studentid
    grades = c.execute("SELECT peeps.id, courses.mark FROM courses, peeps WHERE courses.id = peeps.id and peeps.id = " + str(studentid))
    for row in grades:
        studentinfo.setdefault(key, [])
        studentinfo[key].append(row[1])
    return studentinfo[key]

# creates a dictionary with the studentid as the key and their averages as the value
def makeAverage():
    avg={}
    # The two lines below are a work around for an issue we faced.
    # When we tried allpeeps = c.execute("SELECT peeps.id FROM peeps") and iterated through it,
    # it only returned the first id from the first row
    allPeeps = c.execute("SELECT COUNT(id) FROM peeps")
    for i in range(1,allPeeps.fetchone()[0]+1):
        avg[i] = getAverage(lookAtGrade(i))
    return avg

# computes the average of a list rounded to two decimal places
def getAverage(list):
    sum = 0
    for i in list:
        sum += i
    return round ( (sum * 1.0 / len(list)) , 2)

# Creates an array of each students'information
def makeInfoArray():
    #initializes array
    peepsInfo = []
    averages = makeAverage()
    names = c.execute("SELECT peeps.name, peeps.id FROM peeps")
    for row in names:
        thing = {}
        # key value pair for name
        thing["name"] = str(row[0])
        # key value pair for id
        thing["id"] = row[1]
        # key value pair for average
        thing["avg"] = averages[row[1]]
        peepsInfo.append(thing)
    return peepsInfo


# Display each student's name, id, and average
def displayInfo():
    info = makeInfoArray()
    # goes through array of student info and prints their info
    for student in info:
        string = "Name: " + student["name"]
        string += "\nID: " + str(student["id"])
        string += "\nAverage: " + str(student["avg"])
        string += "\n********************"
        print(string)

#==========================================================
# Create a table of IDs and associated averages, named "peeps_avg"
def createTable():
    peepsInfo = makeInfoArray()
    # creates the table named peeps_avg
    c.execute( "CREATE TABLE peeps_avg(userid INTEGER, average REAL)")
    # goes through peepsInfo and adds
    for student in peepsInfo:
        command = "INSERT INTO peeps_avg (userid, average) VALUES (?, ?)"
        values = [(student["id"], student["avg"])]
        c.executemany(command, values)

def addCRows(code, mark, id):
    command = "INSERT INTO courses (code, mark, id) VALUES (?,?,?)"
    values = [(code, mark, id)]
    c.executemany(command, values)

# testing everything!
displayInfo()
createTable()
addCRows('systems', 66, 11)
addCRows('greatbooks', 89, 11)
addCRows('ceramics', 90, 11)
addCRows('physed', 66, 11)
addCRows('physed', 66, 11)


db.commit() #saves changes
db.close() #closes database
