 # _____  _____ _____ _____ _____     _____                              
 #|  __ \|_   _/ ____|_   _|  __ \   / ____|                             
 #| |__) | | || |  __  | | | |  | | | (___   ___ _ ____   _____ _ __ ___ 
 #|  _  /  | || | |_ | | | | |  | |  \___ \ / _ \ '__\ \ / / _ \ '__/ __|
 #| | \ \ _| || |__| |_| |_| |__| |  ____) |  __/ |   \ V /  __/ |  \__ \
 #|_|  \_\_____\_____|_____|_____/  |_____/ \___|_|    \_/ \___|_|  |___/
 #
from rigidMaster import User, Server, GameServer, RigidDBConnector, Admin

class Main:
    def __init__(self):

        my_user = User("test2","")
        #my_user.register("rigid123")
        my_user.login("rigid123") #login


        #admin = Admin("test1","")
        #admin.login("rigid123")
        #admin.unban("test2")

        #my_user.deployServer("Rigid Custom Game Server")
        #my_user.displayServers()

if (__name__ == "__main__"):
    main = Main()