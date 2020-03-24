from rigidMaster import User, Server, GameServer, RigidDBConnector, Admin

class Main:
    def __init__(self):

        my_user = User("test1","test_user@rigid.com")
        #my_user.register("rigid123")
        my_user.login("rigid123") #login


        #admin = Admin("test1","")
        #admin.login("rigid123")

        #my_user.deployServer("Rigid Custom Game Server")
        my_user.displayServers()

if (__name__ == "__main__"):
    main = Main()