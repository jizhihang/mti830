import re
import json
from sets import Set

mai = []
juin = []
juillet = []
aout = []
septembre = []

arr = [mai, juin, juillet, aout, septembre]

with open('data/airquality1.csv') as openfileobject:
    i = 0
    for line in openfileobject:
        s = line.split(',')
        if i == 0:
            headers = s
        else:
            if s[1] != "NA":
            	arr[int(s[5])-5].append(s[1])
        i += 1

m = max(len(arr[0]), len(arr[1]), len(arr[2]), len(arr[3]), len(arr[4]))

print arr


# Writing pensions file
fAir = open('airquality1337.csv', 'w')
fAir.write('"Mai","Juin","Juillet","Aout","Septembre"\r\n')
j = 0
s = ""
while j<m:
	for i in xrange(0,5):
		if (j<len(arr[i])):
			s += str(arr[i][j])	
		else:
			s += '""'
		if(i<4):
			s += ','
		else:
			s += "\r\n"
		fAir.write(s)
		s = ""
	j += 1
	pass
#fAir.write( json.dumps( datasets['Canada Pension Plan (CPP) and Quebec Pension Plan (QPP)'] ) )
fAir.close()