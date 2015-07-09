#!/home/simon/Workspace/MTI830/exercicepython/env/local/lib/python2.7
from matplotlib import powerLaw
from matplotlib import plotPowerLaws
from nltk.corpus import gutenberg
from nltk.corpus import brown
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from collections import defaultdict
from time import sleep
import numpy as np

def gutenFreq():
    # Obtain the list of words 
    gutenberg_words = gutenberg.raw().split(' ')

    num_gutenberg_words = len(gutenberg_words)
    print "We have "+str(num_gutenberg_words)+" gutenberg words"
    counter=0

    gutenberg_frequ = defaultdict(int)

    sleep(2)
    for word in gutenberg_words:
        counter+=1
        gutenberg_frequ[word]+=1
        if counter%1000 == 0:
            print "Progress : "+str((counter/float(num_gutenberg_words)) *100)+" %"

    gutenberg_frequ = sorted(gutenberg_frequ.values(),reverse=True)
    gutenberg_rank = np.array(xrange(1,len(gutenberg_frequ)+1))

    c, alpha = powerLaw(gutenberg_frequ, gutenberg_rank)
    plotPowerLaws(gutenberg_rank, gutenberg_frequ, [c,c], [-1,-alpha], title="Relation between word rank and frequency for gutenberg", xlabel="Word Rank", ylabel="Word Frequency")

    return 0

def gutenFreqListNoStop():
    # Obtain the list of words 
    gutenberg_words = gutenberg.raw().split(' ')
    englishstop = stopwords.words('english')
    filtered_gutenberg_words = [w for w in gutenberg_words if not w in englishstop]

    num_gutenberg_words = len(filtered_gutenberg_words)
    print "We have "+str(num_gutenberg_words)+" gutenberg filtered words"
    counter=0

    gutenberg_frequ = defaultdict(int)

    sleep(2)
    for word in filtered_gutenberg_words:
        counter+=1
        gutenberg_frequ[word]+=1
        if counter%1000 == 0:
            print "Progress : "+str((counter/float(num_gutenberg_words)) *100)+" %"

    gutenberg_frequ = sorted(gutenberg_frequ.values(),reverse=True)
    gutenberg_rank = np.array(xrange(1,len(gutenberg_frequ)+1))

    c, alpha = powerLaw(gutenberg_frequ, gutenberg_rank)
    plotPowerLaws(gutenberg_rank, gutenberg_frequ, [c,c], [-1,-alpha], title="Relation between word rank and frequency for gutenberg, no stop words", xlabel="Word Rank", ylabel="Word Frequency")

    return 0

def brownFreq():
    # Obtain the list of words 
    brown_words = brown.raw().split(' ')
    
    num_brown_words = len(brown_words)
    print "We have "+str(num_brown_words)+" brown words"
    counter=0

    brown_frequ = defaultdict(int)
    sleep(2)
    for word in brown_words:
        counter+=1
        brown_frequ[word]+=1        
        if counter%1000 == 0:
            print "Progress : "+str((counter/float(num_brown_words)) *100)+" %"
    
    brown_frequ = sorted(brown_frequ.values(),reverse=True)
    brown_rank = np.array(xrange(1,len(brown_frequ)+1))
    
    c, alpha = powerLaw(brown_frequ, brown_rank)
    plotPowerLaws(brown_rank, brown_frequ, [c,c], [-1,-alpha], title="Relation between word rank and frequency for brown", xlabel="Word Rank", ylabel="Word Frequency")

    return 0

def brownFreqListNoStop():
    # Obtain the list of words 
    brown_words = brown.raw().split(' ')
    englishstop = stopwords.words('english')
    filtered_words = [w for w in brown_words if not w in englishstop]
    
    num_filtered_words = len(filtered_words)
    print "We have "+str(num_filtered_words)+" brown filtered words"
    counter=0

    brown_frequ = defaultdict(int)
    sleep(2)
    for word in filtered_words:
        counter+=1
        brown_frequ[word]+=1        
        if counter%1000 == 0:
            print "Progress : "+str((counter/float(num_filtered_words)) *100)+" %"
    
    brown_frequ = sorted(brown_frequ.values(),reverse=True)
    brown_rank = np.array(xrange(1,len(brown_frequ)+1))
    
    c, alpha = powerLaw(brown_frequ, brown_rank)
    print 'According to Zipfs law %.2f should be close to 1.' % alpha
    plotPowerLaws(brown_rank, brown_frequ, [c,c], [-1,-alpha], title="Relation between word rank and frequency for brown, no stop words", xlabel="Word Rank", ylabel="Word Frequency")

    return 0

if __name__ == '__main__':
    brownFreq()
    brownFreqListNoStop()
    gutenFreq()
    gutenFreqListNoStop()
