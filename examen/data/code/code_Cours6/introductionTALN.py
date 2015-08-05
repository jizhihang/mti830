
# coding: utf-8

# #Introduction au TALN en python

# ###Représentation du texte:

# In[1]:

s1 = 'Bonjour tout le monde'
#print s1


# In[2]:

print s1


# In[3]:

s2 = "Hello world"
print s2


# ### une string est vu comme un array, alors on peut voir sa longeur et acceder aux éléments par des index

# In[5]:

print len(s2)


# In[6]:

print s1[0]


# In[8]:

s1[0:9]


# In[6]:

print s1[5:]


# In[34]:

print s1[:7]


# ### De la même façon que R, python nous permet de convertir les charactères en minuscules ou majuscules 

# In[7]:

s3 = s1.upper()
print s3


# In[9]:

s4 = s3.lower()
print s4


# In[10]:

print s4.find('o')


# ###Comme dans d'autres langages de programmation, la concatenation se fait en utilisant l'opérateur "+"

# In[23]:

s1 = 'Bonjour'
s2 = 'tout'
s3 = 'le'
s4 = 'monde'
s5 = s1+s2+s3+s4
print s5


# In[24]:

s0 = ' '
s6 = s1+s0+s2+s0+s3+s0+s4
print s6


# #### opérateur *
# 

# In[25]:

s7 = s6*3
print s7


# Pour le traitement de texte, on préfère avoir une phrase comme une liste de strings 

# In[33]:

s1 = "L'essentiel est \"invisible\" pour les yeux."
s1 = s1.upper()


# In[34]:

print s1
print len(s1)


# In[35]:

s1 = s1.split()
print s1


# ### Les mots sont représentés par des strings
# ### les phrases on va les représenter par des listes de strings

# In[26]:

print s1.index('pour')


# In[28]:

print 'est' in s1


# In[29]:

print len(s1)


# ###Normaliser le text

# In[36]:


s1_min = [w.lower() for w in s1]
print s1_min


# In[37]:

s6 = 'Bonjour'


# In[42]:

s6.endswith('oul')


# # NLTK : Natural language tool kit
# 

# In[43]:

import nltk 


# In[44]:

s1 = 'Hello, my name is Erick'
s2 = s1.split()


# In[45]:

print s2


# ## Tokenization avec nltk

# In[47]:

nltk.word_tokenize(s1)


# ####Quelle est la différence antre le tokenizer de nltk et la fonction split d'un string?

# ###Les stopwords 

# In[48]:

from nltk.corpus import stopwords


# In[49]:

frenchStopWords = stopwords.words('french')
englishStopWords = stopwords.words('english')
spanishStopWords = stopwords.words('spanish')


# In[50]:

def printListOfWords(listOfWords):
    for w in listOfWords:
        print w
    return
    


# In[ ]:




# In[6]:

#printListOfWords(frenchStopWords)


# In[ ]:




# In[5]:

#printListOfWords(spanishStopWords)


# In[4]:

#printListOfWords(englishStopWords)


# In[54]:

from nltk.book import *


# In[138]:

#print text7.tokens


# ###Compter le vocabulaire:

# In[122]:

#print text7.tokens


# In[123]:

print text7.count('said')


# ###Distribution de la frequence des mots

# In[60]:

frecList = FreqDist(text7)
frecList ## les outcomes c'est le nombre de mots


# In[61]:

vocabulary = frecList.keys()
print vocabulary[:50]


# In[62]:

frecList.plot(50,cumulative=False)


# ## mais le graphe montre beaucoup de stop words... alors que peut-on faire?

# In[63]:

# 1 on normalise le text
text7_m = [w.lower() for w in text7]


# In[139]:

#print text7_m


# In[64]:

text7_SansStW = [w for w in text7_m if w not in englishStopWords]


# In[65]:

frecList2 = FreqDist(text7_SansStW,)


# In[66]:

vocabulary2 = frecList2.keys()


# In[3]:

#vocabulary2[:50]


# In[68]:


frecList2.plot(50,cumulative=False)


# ##Les stemmers en python

# In[70]:

from nltk.stem.porter import *


# In[ ]:




# In[71]:

stemmer = PorterStemmer()


# In[72]:

plurals = ['caresses', 'flies', 'dies', 'mules', 'denied',
           'died', 'agreed', 'owned', 'humbled', 'sized',
           'meeting', 'stating', 'siezing', 'itemization',
           'sensational', 'traditional', 'reference', 'colonizer',
           'plotted']
singular = []


# In[73]:

for plural in plurals:
    singular.append(stemmer.stem(plural))


# In[74]:

print singular


# In[75]:

from nltk.stem.snowball import SnowballStemmer


# In[76]:

print(" ".join(SnowballStemmer.languages))


# In[77]:

steemerFr = SnowballStemmer("french") 


# In[78]:

steemerFr.stem('finissons')


# In[83]:

steemerFr.stem(u'chats')


# ##Lemmatizer de WordNet

# In[84]:

wnl = nltk.WordNetLemmatizer()


# In[85]:

[wnl.lemmatize(t) for t in plurals]


# In[86]:

wnl.lemmatize('lions')


# ##Étiquetage de classes lexicales

# In[87]:

text = "Jonh gave the book to Anne"
text = nltk.word_tokenize(text)
print text


# In[88]:

tag_text = nltk.pos_tag(text)


# In[94]:

tag_text[0][1]


# In[89]:

text7_pos = nltk.pos_tag(text7_SansStW)


# In[1]:

#print text7_pos
#choses_elever = [',','%']


# In[117]:

#[w for w in text7_m if w not in englishStopWords]

verbs_t = [t for t in text7_pos if t[1].startswith('M')]


# In[2]:

#print verbs_t


# In[119]:

verbs =[w[0] for w in verbs_t]


# In[120]:

frecVerbs = FreqDist(verbs)


# In[121]:

frecVerbs.plot(50,cumulative=False)


# In[161]:

frecVebsK = frecVerbs.keys()


# In[101]:

nouns_t = [t for t in text7_pos if t[1].startswith('N')]
print len(nouns_t)
nouns =[w[0] for w in nouns_t]
frecNouns = FreqDist(nouns)
frecNouns.plot(50, cumulative=False)


# Regarder la référence:  Natural language processing with Python, by Steven Bird, Ewan Klein, and Edward Loper

# In[ ]:



