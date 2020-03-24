import json

from .db import RigidDBConnector


class Server:
    serverID = ""
    serverName = ""
    serverOwnerID = ""

    def __init__(self, name:str, owner:int):

        self.serverName = name
        self.serverOwnerID = owner

    def deploy(self):
        rigidDB = RigidDBConnector('rigid','server')

        #get counter 
        nextSequence = RigidDBConnector("rigid","counter").findOne(
            {
                "$and": [
                    {"collectionName": "server"},
                    { "columnName": "_id"}
                ]
            }
        )['sequenceValue'] + 1

        #insert server into database
        rigidDB.insert(
            { 
                "_id": int(nextSequence),
                "serverName": self.serverName,
                "serverOwnerID": self.serverOwnerID
            }
        )

        #update the counter
        RigidDBConnector("rigid","counter").update(
            {
                "$and": [
                    {
                        "collectionName": "server"
                    },
                    {
                         "columnName": "_id"
                    }
                ]
            },{
                "$inc": {
                    "sequenceValue": 1
                }
            })

        
        self.serverID = nextSequence

        #update user linked to the deployed server
        RigidDBConnector('rigid','user').update(
            {
                "_id": self.serverOwnerID
            },{
                "$push": {
                    "userServers": self.serverID
                }
            }
        )
    

        print(self.serverName + " created.")

    def toJSON(self):

        return json.dumps(self.__dict__)


class GameServer(Server):

    def __init__(self, name:str, owner:str):
        Server.__init__(self, name, owner)
