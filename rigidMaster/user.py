from .server import GameServer
from .db import RigidDBConnector
import json

class User:

    userName = ""
    userEmail = ""
    userAuthorized = False
    userRegistered = False

    userObjectOK = False
    userServers = []

    def __init__(self, username:str, email:str):

        self.userName = username
        self.userEmail = email

        self.userObjectOK = True

    def register(self):
        """
            Registers the object
        """

        #get next id from database for user collection
        nextSequence = RigidDBConnector("rigid","counter").findOne({"$and": [{"collectionName": "user", "columnName": "_id"}]})['sequenceValue'] + 1

        rigidDB = RigidDBConnector("rigid","user")

        #insert new user into database
        rigidDB.insert({'_id': nextSequence, 'userName': self.userName, 'userEmail': self.userEmail})

        #update the counter

        RigidDBConnector("rigid","counter").update({"$and": [{"collectionName": "user", "columnName": "_id"}]},{"$inc": {"sequenceValue": 1}})


        self.userRegistered = True

        print(self.userName + " : " + self.userEmail + " registered!")

        self.login()


    def login(self):
        """
            Logs in the User and returns Authorized Object
        """

        self.userAuthorized = True

        print(self.userName + " : " + self.userEmail + " logged in!")

    def deployServer(self, server_name:str, location:str):
        """deploys server in a given location
        
        Arguments:
            server_name {str} -- Name of the server to be deployed
            location {str} -- Location to be deployed
        """
        if self.userAuthorized != True:

            print(self.userName + " not authorized to deploy Server!")
            return

        game_server = GameServer(server_name, location, self.userName)
        game_server.deploy()

        self.userServers.append(game_server)

