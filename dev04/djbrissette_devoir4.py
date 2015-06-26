from collections import defaultdict
from nltk.corpus import brown
from nltk.corpus import gutenberg
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
import numpy
from time import sleep

def powerLaw(y, x):
    """
    'When the frequency of an event varies as power of some attribute of that
    event the frequency is said to follow a power law.' (wikipedia)

    This is represented by the following equation, where c and alpha are
    constants:
    y = c . x ^ alpha

    Args
    --------
    y: array with frequency of events >0
    x: numpy array with attribute of events >0

    Output
    --------
    (c, alpha)

    c: the maximum frequency of any event
    alpha: defined by (Newman, 2005 for details):
        alpha = 1 + n * sum(ln( xi / xmin )) ^ -1
    """
    c = 0
    alpha = .0
 
    if len(y) and len(y)==len(x):
        c = max(y)
        xmin = float(min(x))
        alpha = 1 + len(x) * pow(sum(numpy.log(x/xmin)),-1)
 
    return (c, alpha)

def plotPowerLaws(y, x, c=[], alpha=[], title="", xlabel="Word Rank", ylabel="Word Frequency"):
    """
    Plots the relationship between x and y and a fitted power law on LogLog
    scale.

    Args
    --------
    y: array with frequency of events >0
    x: array with attribute of events >0
    c: array of cs for various power laws
    alpha: array of alphas for various power laws
    """
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
    gutenberg_rank = numpy.array(xrange(1,len(gutenberg_frequ)+1))

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
    gutenberg_rank = numpy.array(xrange(1,len(gutenberg_frequ)+1))

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
    brown_rank = numpy.array(xrange(1,len(brown_frequ)+1))
    
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
    brown_rank = numpy.array(xrange(1,len(brown_frequ)+1))
    
    c, alpha = powerLaw(brown_frequ, brown_rank)
    print 'According to Zipfs law %.2f should be close to 1.' % alpha
    plotPowerLaws(brown_rank, brown_frequ, [c,c], [-1,-alpha], title="Relation between word rank and frequency for brown, no stop words", xlabel="Word Rank", ylabel="Word Frequency")

    return 0

if __name__ == '__main__':
    brownFreq()
    brownFreqListNoStop()
    gutenFreq()
    gutenFreqListNoStop()
