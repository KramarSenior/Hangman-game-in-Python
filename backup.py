from pprint import pprint

pprint("Wpisz słowo do gry:")
word = input("")

pprint(len(word))

index = 0
secretWord = []

for i in secretWord:
    secretWord.append('x')


print(secretWord)

pprint("Podaj litere: ")
letter = input("")

if letter in word:
   for i in word:
       print("test")
