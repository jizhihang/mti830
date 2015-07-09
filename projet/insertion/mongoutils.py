#!/usr/bin/python
import ConfigParser, io, os
from pymongo import MongoClient
from model import clientrecord, jobstatus
from datetime import datetime

def _connect(host="mongodb://localhost:27017/"):
    '''
        Connect to the active mongodb ( currently localhost )
        return the active mongo client
    '''
    return MongoClient(str(host))

def _disconnect(host="mongodb://localhost:27017/"):
    if(MongoClient().is_mongos):
        MongoClient().close()
    
def _create(jsondata, database, collection):
    '''
        Insert ONE record in the specified collection for a given database

        @params
        jsondata: MUST be a valid json string, represents the record to insert
        database: string representing the database name
        collection: string representing the collection name ( must exist in the database )

    '''
    client = _connect()
    create_result = client[str(database)][str(collection)].insert_one(jsondata)
    return create_result

def createRecord.

if __name__ == '__main__':
    ''' 
    vnf1 = vnf.Vnf(vnfid="1",name="Test1", user="user1", password="password1", ip="10.10.10.10")
    vnf2 = vnf.Vnf(vnfid="2",name="Test2", user="user2", password="password2", ip="10.10.10.10")
    vnf3 = vnf.Vnf(vnfid="3",name="Test3", user="user3", password="password3", ip="10.10.10.10")
    vnf4 = vnf.Vnf(vnfid="4",name="Test4", user="user4", password="password4", ip="10.10.10.10")

    listofvnfs = [vnf1.toDict(), vnf2.toDict(), vnf3.toDict(), vnf4.toDict()]

    client1 = clientrecord.Client(clientnumber=1, clientid="", name="TestClient2", vcpenum=len(listofvnfs), listofvnf=listofvnfs)
    client2 = clientrecord.Client(clientnumber=2, clientid="", name="TestClient3", vcpenum=len(listofvnfs), listofvnf=listofvnfs)
    client3 = clientrecord.Client(clientnumber=3, clientid="", name="TestClient4", vcpenum=len(listofvnfs), listofvnf=listofvnfs)
    client4 = clientrecord.Client(clientnumber=4, clientid="", name="TestClient5", vcpenum=len(listofvnfs), listofvnf=listofvnfs)
    client5 = clientrecord.Client(clientnumber=5, clientid="", name="TestClient6", vcpenum=len(listofvnfs), listofvnf=listofvnfs)
    
    create_client_record(jsondata=client1.toDict())
    create_client_record(jsondata=client2.toDict())
    create_client_record(jsondata=client3.toDict())
    create_client_record(jsondata=client4.toDict())
    create_client_record(jsondata=client5.toDict())
    '''
