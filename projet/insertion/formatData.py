import re
import json
from pymongo import MongoClient


client = MongoClient()

db = client.test_database

f = open('govt_data_parsed.json', 'w')

i = 0
arr = []

with open('govt_data.csv') as openfileobject:
    for line in openfileobject:
        s = re.sub(r',(?=[^"]*"(?:[^"]*"[^"]*")*[^"]*$)', " ", line)
        if i == 0:
            headers = s.split(",")
        else:
            objVal = s.split(",")
            arr.append({headers[0]: objVal[0],
                        headers[1]: objVal[1],
                        headers[2]: objVal[2],
                        headers[3]: objVal[3].split('\"')[1],
                        headers[6].split('\r\n')[0]: float(objVal[6].split('\r\n')[0])
                        })
        i += 1
    f.write( json.dumps( arr, sort_keys=True ) )


f.close()
