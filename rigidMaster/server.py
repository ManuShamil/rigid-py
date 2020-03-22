"""
class Location:
    hostLocationString = ""
    hostID = ""
    hostIP = ""

    def __init__(self, location, id, ip):
        self.hostLocationString = location
        self.hostID = id
        self.hostIP = ip"""


class Server:
    serverID = ""
    serverName = ""
    serverLocation = None
    serverOwner = None

    def __init__(self, name:str, loc:str, owner:str):

        self.serverID = id
        self.serverName = name
        self.serverLocation = loc
        self.serverOwner = owner

    def createServer(self):

        print(self.serverName + " created.")


class GameServer(Server):

    def __init__(self, name:str, loc:str, owner:str):
        Server.__init__(self, name, loc, owner)
    
    
    
