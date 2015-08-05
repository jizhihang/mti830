import re
import json

datasets = {}

for y in xrange(1991,2015):
    for m in xrange(1,5):
        fm = str(m*3)
        if m < 4:
            fm = "0" + fm
        datasets[str(y)+"/"+fm] = 0

for y in xrange(1991,2015):
    with open("../data/usdcad" + str(y) + ".csv") as openfileobject:
        i = 0
        m = 1
        sum = 0
        for line in openfileobject:
            s = line #re.sub(r',(?=[^"]*"(?:[^"]*"[^"]*")*[^"]*$)', " ", line)
            if i == 0:
                headers = s.split(";")
            else:
                sum += float(s.split(";")[3])
                if m%3 == 0:
                    datasets[str(y) + "/" + str(format(m, '02d'))] = sum/3
                    sum = 0
                m = m + 1
            i += 1

# Writing USDCAD file
fUSDCAD = open('USDCAD.json', 'w')
fUSDCAD.write( json.dumps( datasets ) )
fUSDCAD.close()


