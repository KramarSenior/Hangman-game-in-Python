from pprint import pprint
import json
import random



def generateWord():
    file = open("data.json")
    d = json.load(file)
    y = random.randrange(0,len(d.keys()))
    w = list(d.keys())
    file.close()
    myList = [w[y], d[w[y]]]
    return myList

print(generateWord()[0])
