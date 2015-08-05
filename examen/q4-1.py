import re
import math
from collections import Counter

def cosine_similarity(vectorA, vectorB):
	cosineResult = 0
	intersection = set(vectorA.keys()) & set(vectorB.keys())
	num = sum([vectorA[x] * vectorB[x] for x in intersection])

	sumA = sum([vectorA[x]**2 for x in vectorA.keys()])
	sumB = sum([vectorB[x]**2 for x in vectorB.keys()])
	denom = math.sqrt(sumA) * math.sqrt(sumB)

	if denom != 0:
		cosineResult = float(num) / float(denom)

	return cosineResult
        

aWord = re.compile(r'\w+')

txtA = "all grown-ups were once children but only few of them remember it"
bowA = Counter(aWord.findall(txtA))
txtB = "all children should be very understanding of grown-ups"
bowB = Counter(aWord.findall(txtB))

print "\n\n\nCosine similarity of :"
print '    "' + txtA + '"'
print '  and'
print '    "' + txtB + '"'
print "is : " + str(cosine_similarity(bowA, bowB))