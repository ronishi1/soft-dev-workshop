# RaJe - Jerry Ye and Ray Onishi
# SoftDev1 pd07
# K #06: StI/O: Divine your Destiny!
# 2018-09-13
from random import uniform

def read(CSVfileR):#taken from Intro II hw!Opens a file and returns the contents of the file in a list of strings
    c = open(CSVfileR,"r")
    CSV =  c.readlines()
    c.close()
    return CSV

File = read("occupations.csv")
def editData(list):#edits the list containing the contents of the csv file to make it easier to parse; returns totalPercentage as a float
    File.pop(0)#Removes column descriptions
    totalString = File[-1]
    totalString = totalString[0:len(totalString) -1]
    totalList = totalString.split(",")
    totalPercentage = float(totalList[1])
    File.pop()#Removes total occupation and percentage
    return totalPercentage#returns total percentage to be stored globally
    
totalPercentage = editData(File)#total percentage is stored globally
#print (totalPercentage)

def makeDict(list):#returns a dictionary using the occupation as the key and the percentage as the value
    d = {}
    for s in list:
        s = s[0:len(s) -1]
        l = []
        if s[0] == '"':#splits the string by double quotation marks if there are commas in the occupation description
            l = s.split('"')
            l.pop(0)
            l[1] = l[1][1:]
        else:#splits the string by commas if there are no commas in the occupation description
            l = s.split(",")
        #print (l)
        d[l[0]] = float(l[1])#Creates the dictionary using the occupation as the key and the percentage as the value
    return d
        
Dict = makeDict(File)
def randOccupation(dict):#returns a random occupation based on percentages in the data
    percent = uniform(0,totalPercentage)#picks a random float from 0 - 99.8
    for x in dict:
        percent -= dict[x]#subtracts each percentage  from the randomly picked percentage from 0 - 99.
        if percent < 0:
            return x
print (randOccupation(Dict))
