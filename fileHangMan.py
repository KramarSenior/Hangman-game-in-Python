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


pprint("Witaj w grze hangman!")
username = input("Wprowadź nazwe użytkownika: ")
#word = input("Wpisz słowo do gry: ")
word = generateWord()[0]


file = open("data.json")
d = json.load(file)

pprint("Szukane słowo składa się z %s liter" %len(word))
pprint("Podpowiedź: %s" %generateWord()[1])
secretWord = []
used = []

for i in word:
    secretWord.append('_')

print(secretWord)

file.close()

cond = 1
while cond < 11:
    index = 0
    howMany = 0
    letter = input("Podaj litere: ")
    letter = letter.lower()
    for i in word:
        if letter == i:
            secretWord[index] = letter
            howMany += 1
        index += 1
    if '_' in secretWord:
        if howMany > 0:
            if letter in used:
                pprint('Ups, już podawałeś tą litere!')
            else:
                print("Brawo! Znalazłeś litery w %s miejscach! Twoje słowo to: %s"  %(howMany, secretWord))
                used.append(letter)
        else:
            if cond == 10:
                pprint("Niestety, przegrałeś! Szukane słowo to: %s" %word)
            else:
                pprint("Niestety, nie zgadłeś! Zostało Ci %s szans" %(10-cond))
                used.append(letter)
            cond += 1
    else:
        cond = 11
        pprint("Wygrałeś!")

print(secretWord)
