from rigidMaster import User, Server, GameServer

class Main:
    def __init__(self):

        my_user = User("rigid_user","rigid_user@rigid.com")
        my_user.register()
        my_user.deployServer("hi","india")

if (__name__ == "__main__"):
    main = Main()