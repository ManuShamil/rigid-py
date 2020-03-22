from .server import GameServer

class User:

    userName = ""
    userEmail = ""
    userAuthorized = False
    userRegistered = False

    userObjectOK = False

    def __init__(self, username:str, email:str):

        self.userName = username
        self.userEmail = email

        self.userObjectOK = True

    def register(self):
        """
            Registers the object
        """

        self.userRegistered = True

        print(self.userName + " : " + self.userEmail + " registered!")

        self.login()


    def login(self):
        """
            Logs in the User and returns Authorized Object
        """

        self.userAuthorized = True

        print(self.userName + " : " + self.userEmail + " logged in!")

    def deployServer(self, server_name, location):
        if self.userAuthorized != True:

            print(self.userName + " not authorized to deploy Server!")
            return

        game_server = GameServer(server_name, location, self.userName)
        game_server.createServer()

