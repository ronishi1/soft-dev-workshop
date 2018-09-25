import csv, random
#function for returning a random key based on the weights in the dict
def randomKey(dict):
    keys = []
    for key in dict:
        if key != 'Job Class':#job class and total arent to be chosen from
            if key != 'Total':
                keys = keys + [key] * int(dict[key] * 10)
                return random.choice(keys)


# creates a dictionary out of occupations.csv
def makeDict(filename):
    occDict = {}
    with open(filename) as file:
        csvReader = csv.reader(file, delimiter = ',')
        for row in csvReader:
            if row[0] != "Job Class":#just to make sure we dont accidentally turn a string into a float
                occDict[row[0]] = float(row[1])
            else:
                occDict[row[0]] = row[1]
    return occDict
