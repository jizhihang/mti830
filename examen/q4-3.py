import math

#	pain,	KFC,	Beer,	Nuts,	Diapers,Wine
matrice = [
	[1,		2,		3,		4,		5,		6],	#Canada
	[5,		12,		1,		0,		5,		12] #USA
]

n = 2

df = [3,2,3,2,3,3]
idf = df
print idf
for i in xrange(0,6):
	idf[i] = math.log(n/df[i])

print idf



tfidf = matrice

for i in xrange(0,6):
	for j in xrange(0,3):
		tfidf[j][i] = matrice[j][i]*idf[i]

print tfidf