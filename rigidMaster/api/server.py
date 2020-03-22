from .user import User

class Server:
    serverID = ""
    serverName = ""
    serverLocation = ""
    serverOwner = None

    def __init__(self, id:str, name:str, loc:str, owner:User):

        self.serverID = id
        self.serverName = name
        self.serverLocation = loc
        self.serverOwner = owner

    def createServer(self):

        print(self.serverName + " created.")


class GameServer(Server):

    def __init__(self, id:str, name:str, loc:str, owner:User):
        Server.__init__(self, id, name, loc, owner)

    
    
    
