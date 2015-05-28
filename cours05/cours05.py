# -*- coding: utf-8 -*-
import nltk
from nltk.book import text6
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

__author__ = 'djb'

def printList(list):
    for w in list:
        print w
    return

tokenizer = RegexpTokenizer(r'\w+')
print tokenizer.tokenize("J'aime beaucoup le pain, car mur!")

frenchStopwords = stopwords.words("french")
spanishStopwords = stopwords.words("spanish")
englishStopwords = stopwords.words("english")

print text6

mytext = nltk.Text(text6)

print mytext