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

def _update(recordID, jsondata, database, collection):
    ''' 
        Update a SINGLE existing client record
        If the record is not found, error message will be returned
    '''
    client = _connect()
    update_result = client[str(database)][str(collection)].update({"_id", recordID}, jsondata)
    return update_result

def _readall(database, collection):
    '''
        Read all the records for the specified collection of the specified database
    '''
    client = _connect()
    cursor = client[str(database)][str(collection)].find()
    return cursor

def _readone(database, collection, criteria):
    '''
        Read one record from the database depending on the given criteria
            It should be the "_id" field if you want to be sure you have the right record !
    '''
    return 0 
    
def create_client_record(clientnumber, clientname, numberofvcpe, vcpelogin, vcpepwd):
    '''
        Insert a new client record.
        When calling this method, it is assumed we are using the BOSDB database and the clients collection
        This is not a generic method, I suggest creating your own using _create if you have different needs
    '''
    listofvnfs = []
    for index in range(numberofvcpe):
        vnfid = str(clientname)+"vnf"+str(index)
        vnfname = str(clientname)+str(index)
        # Notice we are not passing the object directly, but the toDict() method
        listofvnfs.append(clientrecord.Vnf(vnfid=vnfid,name=vnfname, user=vcpelogin, password=vcpepwd, ip="tobeupdated").toDict())

    client = clientrecord.Client(clientnumber=clientnumber, clientid="", name=clientname, vcpenum=len(listofvnfs), listofvnf=listofvnfs)
    clientData = client.toDict()

    # Delete the "_id" because we want MongoDB to generate it, but we need it in the object for read operations
    # It's not 100% idiotic to do this but it's not 100% intelligent either

    if("_id" in clientData):
        clientData.pop("_id", None)

    return _create(jsondata=clientData, database="bosdb", collection="clients")

def create_job(clientid, clientname, numberofinstances, username, password):
    '''
        Create an empty job record with a number of instances corresponding to the number of vnf's ordered by the client
        This record will later be used to update the deployment status
        The job record ID is returned by the creation method, it is the unique identifier in the dabatase, don't lose it ! 
    '''
    listofinstances = []
    for index in range(numberofinstances):
        instanceName = str(clientname) + str("-vCPE-") + str(index)
        listofinstances.append(jobstatus.InstanceBuildStatus(start_ts = datetime.today().isoformat(' '),
                                                             end_ts = datetime.today().isoformat(' '),
                                                             name = instanceName,
                                                             percent = 0,
                                                             ping_count = 0,
                                                             status = "",
                                                             mgmt_ip = "",
                                                             user = username,
                                                             password = password).toDict())
    
    overallBuildStatus = jobstatus.OverallBuildStatus(overall_id = "",
                                                      client_id = clientid,
                                                      start_ts = datetime.today().isoformat(' '), 
                                                      end_ts = datetime.today().isoformat(' '), 
                                                      percent = 0, 
                                                      status = "", 
                                                      instances = listofinstances)
    overallBuildData = overallBuildStatus.toDict()

    if("_id" in overallBuildData):
        overallBuildData.pop("_id", None)

    return _create(jsondata=overallBuildData, database="bosdb", collection="status")
        
def update_client_record(clientID, jsondata):
    '''
        Fully replace the existing client record for a given client id
    '''
    return _update(clientID, jsondata=jsondata, database="bosdb", collection="clients")


def update_status_record(jobID, jsondata):
    '''
        Fully replace the existing status record for a given job id
    '''
    return _update(jobID, jsondata=jsondata, database="bosdb", collection="status")

def read_all_clients():
    '''
        Read the complete collection of clients
        Return all results
    '''
    return _readall(database="bosdb", collection="clients")

def get_client_count():
    '''
        Return the number of client records in the "clients" collection
    '''
    mongoclient = _connect()
    count = mongoclient['bosdb']['clients'].count()
    return count

def delete_client_record(clientID):
    '''
    Read the clients.bos parameters file and return a dict of dict
    Dict of client
        containing dict of parameters=value for said client
    '''

    return 0 

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
