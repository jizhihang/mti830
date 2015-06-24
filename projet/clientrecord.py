import json

class Client(object):
    def __init__(self, clientnumber, clientid, name, vcpenum, listofvnf):
        self.clientnumber = clientnumber
        self.clientid = clientid
        self.name = name
        self.vcpenum = vcpenum
        self.vnfs = listofvnf

    def toDict(self):
        '''
            Returns the class attributes in the form of a python dict
        '''
        data = { 
                 "_id": self.clientid,
                 "number": self.clientnumber,
                 "name": self.name,
                 "vcpenum": self.vcpenum,
               }

        # Add the vnflist dicts to the client record
        
        for index in range(len(self.vnfs)):
            key = "vnf{}".format(index)
            data[key] = self.vnfs[index]

        return data

    def toJson(self):
        '''
            Takes the class attributes, puts them in a dict and return a properly formatted JSON string
        '''
        return json.dumps(self.toDict(), indent=4, separators=(',',': '))

class Vnf(object): 
    ''' 
        Class that represents a database record for a vnf assigned to a client
        Phase 1 of the project, it's a vCPE
    '''

    def __init__(self, vnfid,name="vnfname", user="user", password="password", ip="192.168.0.1"):
        ''' 
            Constructor for the class
            No need for getters / setters, all the attributes can be accessed from anywhere
        '''
        self.vnfid = vnfid
        self.name = name
        self.user = user
        self.password = password
        self.ip = ip

    def toDict(self):
        ''' 
            Returns the class attributes in the form of a python dict
            I believe this way is easier to use if you want to embed this object data in another object
                this way the JSON formatting will only be done at one place, and all at the same time
        '''
        data = { "_id" : self.vnfid,
                 "name": self.name,
                 "user": self.user,
                 "password": self.password,
                 "ipaddress": self.ip
                }
        return data

    def toJson(self):
        '''
            Takes the class attributes, puts them in a dict and return a properly formatted JSON string
        '''
        data = { "_id" : self.vnfid,
                 "name": self.name,
                 "user": self.user,
                 "password": self.password,
                 "ipaddress": self.ip
                }
        return json.dumps(data, indent=4, separators=(',',': '))
