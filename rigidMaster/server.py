import json

from .db import RigidDBConnector


class Server:
    serverID = ""
    serverName = ""
    serverOwner = ""

    def __init__(self, name:str, owner:str):

        self.serverName = name
        self.serverOwner = owner

    def deploy(self):
        rigidDB = RigidDBConnector('rigid','server')

        nextSequence = RigidDBConnector("rigid","counter").findOne(
            {
                "$and": [
                    {"collectionName": "server"},
                    { "columnName": "_id"}
                ]
            }
        )['sequenceValue'] + 1

        rigidDB.insert(
            { 
                "_id": int(nextSequence),
                "serverName": self.serverName,
                "serverOwner": self.serverOwner
            }
        )

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

        print(self.serverName + " created.")

    def toJSON(self):

        return json.dumps(self.__dict__)


class GameServer(Server):

    def __init__(self, name:str, owner:str):
        Server.__init__(self, name, owner)
