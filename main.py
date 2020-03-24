from rigidMaster import User, Server, GameServer, RigidDBConnector, Admin

class Main:
    def __init__(self):

        my_user = User("","rigid_user@rigid.com")
        #my_user.register()
        #my_user.login("rigid123") #login


        admin = Admin("rigid_user","")
        admin.login("rigid123")

        #my_user.deployServer("Rigid Custom Game Server")

        print(admin.__dict__)

if (__name__ == "__main__"):
    main = Main()