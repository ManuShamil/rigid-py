from .server import GameServer
from .db import RigidDBConnector
import json
import bcrypt

class User:

    userName = ""
    userEmail = ""
    userHashedPassword = ""

    userAuthorized = False
    userRegistered = False

    userObjectOK = False
    userServers = []

    def __init__(self, username:str, email:str, password:str):

        self.userName = username
        self.userEmail = email
        self.userHashedPassword = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        self.userObjectOK = True

    def register(self):
        """
            Registers the object
        """

        #check if username/email already exists in database
        duplicate = RigidDBConnector("rigid","user").findOne({"$or": [{"userName": self.userName}, {'userEmail': self.userEmail}]})
        if (duplicate != None):
            print("{0} : {1} already exists in database!".format(self.userName, self.userEmail))

            return

        #get next id from database for user collection
        nextSequence = RigidDBConnector("rigid","counter").findOne({"$and": [{"collectionName": "user", "columnName": "_id"}]})['sequenceValue'] + 1

        rigidDB = RigidDBConnector("rigid","user")

        #insert new user into database
        rigidDB.insert({'_id': nextSequence, 'userName': self.userName, 'userEmail': self.userEmail, 'userHashedPassword': self.userHashedPassword})

        #update the counter

        RigidDBConnector("rigid","counter").update({"$and": [{"collectionName": "user", "columnName": "_id"}]},{"$inc": {"sequenceValue": 1}})


        self.userRegistered = True

        print(self.userName + " : " + self.userEmail + " registered!")


    def login(self, password:str):
        """
            Logs in the User and returns Authorized Object
        """
        hashedPassword = RigidDBConnector("rigid","user").findOne({ "$or": [{"userName": self.userName}, {"userEmail": self.userEmail}]})['userHashedPassword']

        if bcrypt.checkpw(password.encode('utf-8'), hashedPassword):
            self.userHashedPassword = hashedPassword

            self.userAuthorized = True
            
            print("{0} succesfully logged in!".format(self.userName))
        else:
            self.userAuthorized = False
            
            print("{0} could be not logged in".format(self.userName))

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

