from collections import defaultdict
from nltk.corpus import brown
from nltk.corpus import gutenberg
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
import numpy
from time import sleep

#code found on github
def plotPowerLaws(y, x, c=[], alpha=[], title="", xlabel="Word Rank", ylabel="Word Frequency"):
    import matplotlib.pyplot as plt

    plt.figure()
    plt.loglog()
    plt.plot(x,
             y,
             'r+')
    for _c, _alpha in zip(c,alpha):
        plt.plot( (1, max(x)),
                  (_c, _c * pow(max(x), _alpha)),
                  label='~x^%.2f' % _alpha)
        plt.legend()
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

#code found on github
def powerLaw(y, x):
    c = 0
    alpha = .0
 
    if len(y) and len(y)==len(x):
        c = max(y)
        xmin = float(min(x))
        alpha = 1 + len(x) * pow(sum(numpy.log(x/xmin)),-1)
 
    return (c, alpha)

#   stop words
stopWords = stopwords.words("english")
#   Gutenberg corpus
gutenWords = gutenberg.raw().split(" ")
gutenFreq = defaultdict(int)
#   Without stopwords
gutenFilteredFreq = defaultdict(int)
gutenWordsFiltered = [w for w in gutenWords if not w in stopWords]
#   Frequencies
for w in gutenWords:
    gutenFreq[w] += 1
gutenFreq = sorted(gutenFreq.values(), reverse=True )
#   Word ranks
gutenRank = numpy.array(xrange(1, len(gutenFreq)+1 ))
c, a = powerLaw(gutenFreq, gutenRank)
plotPowerLaws(gutenRank, gutenFreq, [c, c], [-1, -a], "Word rank inversely proportional to word frequency (Gutenberg)", "Word rank", "Word frequency")

for w in gutenWordsFiltered:
    gutenFilteredFreq[w] += 1
gutenFilteredFreq = sorted(gutenFilteredFreq.values(), reverse=True)
#   Filtered word ranks
gutenFilteredRank = numpy.array(xrange(1, len(gutenFilteredFreq)+1 ))
c, a = powerLaw(gutenFilteredFreq, gutenFilteredRank)
plotPowerLaws(gutenFilteredRank, gutenFilteredFreq, [c, c], [-1, -a], "Word rank inversely proportional to word frequency (Gutenberg without stopwords)", "Word rank", "Word frequency")

#   Brown corpus
brownWords = brown.raw().split(" ")
#   Without stopwords
brownWordsFiltered = [w for w in brownWords if not w in stopWords]
#   Frequencies
brownFreq = defaultdict(int)
brownFilteredFreq = defaultdict(int)
for w in brownWords:
    brownFreq[w] += 1
brownFreq = sorted(brownFreq.values(), reverse=True )
#   Word ranks
brownRank = numpy.array(xrange(1, len(brownFreq)+1 ))
c, a = powerLaw(brownFreq, brownRank)
plotPowerLaws(brownRank, brownFreq, [c, c], [-1, -a], "Word rank inversely proportional to word frequency (Brown)", "Word rank", "Word frequency")

for w in brownWordsFiltered:
    brownFilteredFreq[w] += 1
brownFilteredFreq = sorted(brownFilteredFreq.values(), reverse=True )
#   Word ranks
brownFilteredRank = numpy.array(xrange(1, len(brownFilteredFreq)+1 ))
c, a = powerLaw(brownFilteredFreq, brownFilteredRank)
plotPowerLaws(brownFilteredRank, brownFilteredFreq, [c, c], [-1, -a], "Word rank inversely proportional to word frequency (Brown without stopwords)", "Word rank", "Word frequency")
