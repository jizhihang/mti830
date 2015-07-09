import re
import json
from pymongo import MongoClient
from sets import Set

def find_by_ref_date(arr, ref_date):
    for obj in arr:
        if obj['Ref_Date'] == ref_date:
            return obj
    return False



datasets = {
    'Canada Pension Plan (CPP) and Quebec Pension Plan (QPP)': [],
    'Federal government': [],
    'Consolidated government': [],
    'Local government': [],
    'Provincial and territorial government': []
}

with open('govt_data.csv') as openfileobject:
    i = 0
    for line in openfileobject:
        s = re.sub(r',(?=[^"]*"(?:[^"]*"[^"]*")*[^"]*$)', " ", line)
        if i == 0:
            headers = s.split(",")
        else:
            objVal = s.split(",")
            ref_date = objVal[0]
            statement = objVal[3].split('\"')[1]
            value = float(objVal[6].split('\r\n')[0])
            obj = find_by_ref_date(datasets[objVal[2]], ref_date)
            if obj == False:
                datasets[objVal[2]].append({"Ref_Date": ref_date, statement: value})
            else:
                obj[statement] = value
        i += 1

# Writing pensions file
fPensions = open('govt_data_matrix_pensions.json', 'w')
fPensions.write( json.dumps( datasets['Canada Pension Plan (CPP) and Quebec Pension Plan (QPP)'] ) )
fPensions.close()

# Writing Federal file
fFederal = open('govt_data_matrix_federal.json', 'w')
fFederal.write( json.dumps( datasets['Federal government'] ) )
fFederal.close()

# Writing Consolidated file
fConsolidated = open('govt_data_matrix_consolidated.json', 'w')
fConsolidated.write( json.dumps( datasets['Consolidated government'] ) )
fConsolidated.close()

# Writing Local file
fLocal = open('govt_data_matrix_local.json', 'w')
fLocal.write( json.dumps( datasets['Local government'] ) )
fLocal.close()

# Writing Provincial file
fProvincial = open('govt_data_matrix_provincial.json', 'w')
fProvincial.write( json.dumps( datasets['Provincial and territorial government'] ) )
fProvincial.close()




