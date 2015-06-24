from nltk.corpus import gutenberg
from nltk.corpus import brown

text = gutenberg.raw()
text_tokens = nltk.word_tokenize(text)
frecList_gutenberg = FreqDist(text_tokens)
text_brown = brown.raw()
text_brown_tokens = nltk.word_tokenize(text_brown)
frecList_brown = FreqDist(text_tokens)ten