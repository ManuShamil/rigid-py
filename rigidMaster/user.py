from .server import GameServer
from .db import RigidDBConnector
import json
import bcrypt
from tabulate import tabulate

class User:
    userID = ""
    userName = ""
    userEmail = ""
    userHashedPassword = ""

    userAuthorized = False
    userRegistered = False

    userObjectOK = False
    userServers = []

    def __init__(self, username:str, email:str):

        self.userName = username
        self.userEmail = email

        self.userObjectOK = True

    def register(self, password):
        """
            Registers the user into database
        """

        isOK = self.userName != "" and self.userEmail != ""

        if isOK != True:
            
            print("Username or Email cannot be empty.")

            return

        self.userHashedPassword = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        #check if username/email already exists in database
        duplicate = RigidDBConnector("rigid","user").findOne(
            {
                "$or": [
                    {
                        "userName": self.userName
                    },
                    {
                        'userEmail': self.userEmail
                    }
                ]
            }
        )

        if (duplicate != None):
            print("{0} : {1} already exists in database!".format(self.userName, self.userEmail))

            return

        #get next id from database for user collection
        nextSequence = RigidDBConnector("rigid","counter").findOne(
            {
                "$and": [
                    {   
                        "collectionName": "user" 
                    },
                    {
                        "columnName": "_id"
                    }
                ]
            }
        )['sequenceValue'] + 1

        rigidDB = RigidDBConnector("rigid","user")

        #insert new user into database
        rigidDB.insert(
            {
                '_id': int(nextSequence),
                'userName': self.userName,
                'userEmail': self.userEmail,
                'userHashedPassword': self.userHashedPassword,
                'userServers': self.userServers
            })

        #update the counter
        RigidDBConnector("rigid","counter").update(
            {
                "$and": [
                    {   
                        "collectionName": "user" 
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


        self.userID = nextSequence #nextSequence is the id of the user just inserted
        self.userRegistered = True

        print(self.userName + " : " + self.userEmail + " registered!")


    def login(self, password:str):
        """Logs in the User and returns Authorized Object
        
        Arguments:
            password {str} -- Password of the user
        """

        userData = RigidDBConnector("rigid","user").findOne(
            { 
                "$or": [
                    {
                        "userName": self.userName
                    },{
                        "userEmail": self.userEmail
                    }
                ]
            })

        if userData == None:

            print("User does not exist in Database!")
            return

        if "isBanned" in userData:
            if userData['isBanned'] is True:

                print("You have been restricted from logging in. Please contact customer support!")
                return

        if bcrypt.checkpw(password.encode('utf-8'), userData['userHashedPassword']):
            self.userHashedPassword =  userData['userHashedPassword']

            self.userID = int(userData['_id'])
            self.userName = str(userData['userName'])
            self.userEmail = str(userData['userEmail'])
            self.userServers = userData['userServers']

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

        game_server = GameServer(server_name, self.userID)
        game_server.deploy()

        self.userServers.append(game_server.serverID)

    def displayServers(self):

        if self.userAuthorized != True:
            
            print('User not logged into retrieve server list.')
            
            return

        myServers = RigidDBConnector('rigid','server').findAll(
            {
                "serverOwnerID": self.userID
            }
        )

        serverList = []

        for x in myServers:
            serverList.append([x["_id"],x["serverName"],x["serverOwnerID"]])

        print(tabulate((serverList),headers=["ID","Server Name","Server Owner ID"], tablefmt="pretty"))
        
        return myServers

class Admin(User):
    adminID = ""
    adminAuthorized = False

    def __init__(self, username:str, email:str):
        User.__init__(self, username, email)

    def login(self, password):
        User.login(self, password) #login as normal user

        if (self.userAuthorized == True): #check if the last login attempt was succesful

            AdminData = RigidDBConnector('rigid','admin').findOne(
                {
                    "userID": self.userID
                }
            )
            
            isAdmin = AdminData != None 

            if isAdmin:
                self.adminID = AdminData['_id']

                self.adminAuthorized = True

                print("{0} succesfully logged in as Admin".format(self.userName))
            
            else:

                print("{0} could not be logged in as Admin!".format(self.userName))
        else:

            print("{0} could not be logged in!".format(self.userName))

    def ban(self,username):
        self.userName=username

        if (self.adminAuthorized != True):
            print("User need to be logged in to perform ban")
            return

        
        RigidDBConnector('rigid','user').update(
            {
               "userName":  username
            },
            {
                "$set": {
                    "isBanned": True
                }
            }
        )

        print("{0} is banned!".format(self.userName))
        
    
    def unban(self,username):
        self.userName=username

        if (self.adminAuthorized != True):
            print("User does not privilege to perform this action")
            return

        
        RigidDBConnector('rigid','user').update(
            {
               "userName":  username
            },
            {
                "$set": {
                    "isBanned": False
                }
            }
        )
 
        print("{0} is unbanned!".format(self.userName))
        
        
        



            


