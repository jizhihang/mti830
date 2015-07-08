import json

class Record(object):
    def __init__(self, p_date, p_geo, p_sector, p_statement, p_vector, p_coordinate, p_value):
        self.date = p_date
        self.geo = p_geo
        self.sector = p_sector
        self.statement = p_statement
        self.vector = p_vector
        self.coordinate = p_coordinate
        self.value = p_value

    def toDict(self):
        '''
            Returns the class attributes in the form of a python dict
        '''
        data = { 
                    "date": self.date,
                    "geo": self.geo,
                    "sector": self.sector,
                    "statement": self.statement,
                    "vector": self.vector,
                    "coordinates": self.coordinate,
                    "value": self.value
               }
        return data

    def toJson(self):
        '''
            Takes the class attributes, puts them in a dict and return a properly formatted JSON string
        '''
        return json.dumps(self.toDict(), indent=4, separators=(',',': '))