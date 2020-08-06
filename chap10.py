import hangman
import csv
import random
words=[]
with open("randam_words.csv","r",encoding="utf_8_sig") as f:
    r=csv.reader(f,delimiter=",")
    for row in r:
        for rowow in row:
            if rowow !="":
                words.append(rowow)
    word=words[random.randint(0,len(words)-1)]
    hangman.hangman(word)
