from rigidMaster import User, Server, GameServer, RigidDBConnector

class Main:
    def __init__(self):

        my_user = User("rigid_user","rigid_user@rigid.com","rigid123")
        my_user.register()
        my_user.login("rigid123") #login

        my_user.deployServer("Arma II")

        print(my_user.__dict__)

if (__name__ == "__main__"):
    main = Main()