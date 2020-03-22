from .api.user import User
from .api.server import Server, GameServer

    
class API:
    def __init__(self):
        print("rigid Master API")

    def createUser(self, name, email):
        """Registers a new user to database
        
        Arguments:
            name {str} -- User name of the user
            email {str} -- Email of the user
        
        Returns:
            User -- Authorized User Object
        """

        user = User(name, email)
        user.register()

        return user

    def loginUser(self, name, email):
        """Logs in user
        
        Arguments:
            name {str} -- User name of the user
            email {str} -- Email of the user
        
        Returns:
            User -- Authorized User Object
        """

        user = User(name, email)
        user.login()

        return user

    def createServer(self, server_name:str, owner:User):

        game_server = GameServer("101", server_name, "India", owner)
        game_server.createServer()

        return game_server
        
        