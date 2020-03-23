from .server import GameServer
from .db import RigidDBConnector
import json
import bcrypt

class User:
    userID = ""
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
        rigidDB.insert({'_id': int(nextSequence), 'userName': self.userName, 'userEmail': self.userEmail, 'userHashedPassword': self.userHashedPassword})

        #update the counter

        RigidDBConnector("rigid","counter").update({"$and": [{"collectionName": "user", "columnName": "_id"}]},{"$inc": {"sequenceValue": 1}})


        self.userID = nextSequence #nextSequence is the id of the user just inserted
        self.userRegistered = True

        print(self.userName + " : " + self.userEmail + " registered!")


    def login(self, password:str):
        """Logs in the User and returns Authorized Object
        
        Arguments:
            password {str} -- Password of the user
        """
        userData = RigidDBConnector("rigid","user").findOne({ "$or": [{"userName": self.userName}, {"userEmail": self.userEmail}]})

        if bcrypt.checkpw(password.encode('utf-8'), userData['userHashedPassword']):
            self.userHashedPassword =  userData['userHashedPassword']

            self.userID = int(userData['_id'])

            self.userAuthorized = True
            
            print("{0} succesfully logged in!".format(self.userName))
        else:
            self.userAuthorized = False
            
            print("{0} could be not logged in".format(self.userName))

    def deployServer(self, server_name:str):
        """deploys server in a given location
        
        Arguments:
            server_name {str} -- Name of the server to be deployed
            location {str} -- Location to be deployed
        """
        if self.userAuthorized != True:

            print(self.userName + " not authorized to deploy Server!")
            return

        game_server = GameServer(server_name, self.userName)
        game_server.deploy()

        self.userServers.append(game_server)

        RigidDBConnector('rigid','user').update({"$or": [{"userName": self.userName}, {"userEmail": self.userEmail}]}, { "$push": {"userServers": game_server.toJSON()}})


