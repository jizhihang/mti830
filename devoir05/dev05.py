import re

words = []


with open('4news_dictionary.txt') as openfileobject:
	for line in openfileobject:
		obj = {}
		obj["word"] = re.findall(r"\s+\d+\s+(\w+)", line)[0]
		words.append(obj)

i=0
with open('p1.csv') as openfileobject:
	for line in openfileobject:
		matches = re.findall(r"(.+),(.+),(.+),(.+)", line)
		words[i]["freq1"] = float(matches[0][0])
		words[i]["freq2"] = float(matches[0][1])
		words[i]["freq3"] = float(matches[0][2])
		words[i]["freq4"] = float(matches[0][3])
		i += 1

topic1 = sorted(words, key=lambda x: x["freq1"], reverse=True)
print "Words for topic 1 (the religion of CHRISTIANITY) : "
for i in xrange(0,10):
	print "{} : {}".format(topic1[i]["word"], topic1[i]["freq1"])
print "\r\n\r\n"

topic2 = sorted(words, key=lambda x: x["freq2"], reverse=True)
print "Words for topic 2 (impact of diet on HEALTH) : "
for i in xrange(0,10):
	print "{} : {}".format(topic2[i]["word"], topic2[i]["freq2"])
print "\r\n\r\n"	

topic3 = sorted(words, key=lambda x: x["freq3"], reverse=True)
print "Words for topic 3 (INFORMATION SECURITY in modern democracies) :"
for i in xrange(0,10):
	print "{} : {}".format(topic3[i]["word"], topic3[i]["freq3"])
print "\r\n\r\n"

topic4 = sorted(words, key=lambda x: x["freq4"], reverse=True)
print "Words for topic 4 (SPACE EXPLORATION and discoveries by Nasa) :"
for i in xrange(0,10):
	print "{} : {}".format(topic4[i]["word"], topic4[i]["freq4"])
print "\r\n\r\n"