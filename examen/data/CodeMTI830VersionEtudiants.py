
# coding: utf-8

# ####Code pour examen MTI830 
# *Ce code a été conçu pour python 2.7*

# D'abord nous chargeons les librairies que nous utiliserons

# In[30]:

import glob # for reading files
import sys # for reading files
import os # for path processing
import codecs #for encoding while reading files
#import matplotlib.gridspec as gridspec
import nltk #for nlp tasks
lemmatizer = nltk.wordnet.WordNetLemmatizer()
import numpy as np #for creating matrices and make operations
from sklearn.feature_extraction.text import TfidfVectorizer # for creating a TFIDF matrice
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt # for graphs


# Nous commençons par une fonction qui lit un seul fichier : *readSingleFile*()

# In[2]:

def readSingleFile (fileName):
    contentFile = [] 

    f = codecs.open(fileName, mode = 'rt', encoding='utf-8')
    for line in f:
        contentFile.append(line)
        #contentFile.append(line.split(	))
    
    return contentFile


# Cette fonction permet de lire tous les fichiers contenus dans un dossier: *readAllFiles()*

# In[33]:

def readAllFiles (path):
    newPath = os.getcwd()+path
    allFiles = glob.glob(newPath)
    corpus_Read = []
    for f in allFiles:
        corpus_Read.append(readSingleFile(f))
    return corpus_Read


# Cette fonction retourne le nom de tous les fichiers contenus dans un dossier :

# In[27]:

def getNameOfFiles(path):
    nameOfFiles = []
    newPath = os.getcwd()+path
    allFiles = glob.glob(newPath)
    for f in allFiles:
        ind = len(f.split('/')) -1
        nameOfFiles.append(f.split('/')[ind][0:2])
    return nameOfFiles


# Alors, nous lisons les fichiers et nous les stockons dans **documents**. Le nom des fichiers sera aussi lu, et nous le stockons dans **nameOfFiles**

# In[34]:

path = '/CorpusNYTNews/*.txt'
nameOfFiles = getNameOfFiles(path)
documents = readAllFiles(path)


# Pour créer la matrice TFIDF nous créons la fonction *createTFIDFMatrix*. La variable **collection** doit etre un vecteur de strings, donc chaque string représente un document. La variable **documents** est un vecteur qui contient d'autres vectors, c'est à dire les documents(30), les documents sont un vecteur qui contient des strings. Pour utiliser la fonction *createTFIDFMatrix* nous devrons convertir chaque document à string.
# 

# In[36]:

def createTFIDFMatrix(collection):
    vectorizer = TfidfVectorizer(min_df=1)
    matrix = vectorizer.fit_transform(collection)
    return matrix


# cette fonction,*transformDocumentToString*  transforme les vecteurs de documents en vecteurs de strings 

# In[41]:

def transformDocumentToString(collection):
    stringDocuments = []
    for d in documents:
        sen = ''
        for s in d:
            sen = sen+s
        stringDocuments.append(sen)
    return stringDocuments


# In[42]:

stringDocuments = transformDocumentToString(documents)
tf_idf_matrix = createTFIDFMatrix(stringDocuments)


# Nous applicons SVD sur la matrice résultante:

# In[44]:

dense_string_documents = tf_idf_matrix.todense()
U, s, V = np.linalg.svd(dense_string_documents, full_matrices=True)


# Nous créons la fonction *getXAndYCoordinates* pour récupérer les coordonnées et pouvoir visualiser la postion des documents

# In[45]:

def getXAndYCoordinates(variableOfDocuments):
    coord_x = []
    for c in variableOfDocuments[0:,2]:
        coord_x.append(c.item(0))

    coord_y = []
    for c in variableOfDocuments[0:,3]:
        coord_y.append(c.item(0))
    return coord_x, coord_y


# Dans quelle variable se retrouve les vecteurs correspondants aux documents **U, s ou V**? appelez la fonction *getXAndYCoordinates* avec la variable correcte.

# In[46]:

coord_X,coord_Y = getXAndYCoordinates(U) # ??????????


# Finalement nous visualisons les documents dans un graphique.

# In[50]:

fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(coord_X, coord_Y, 'ro')
i = 0

while i < len(nameOfFiles):
    tag = nameOfFiles[i]
    xy = (coord_X[i],coord_Y[i])
    ax.annotate('%s'%tag, xy=xy, textcoords='offset points')
    i = i+1

plt.show()


# #Bonne chance!!!

# In[ ]:



