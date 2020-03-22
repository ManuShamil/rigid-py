from rigidMaster import API

class Main:
    def __init__(self):

        rigidAPI = API()

        my_user = rigidAPI.createUser("rigid_user","rigid_user@rigid.com")

        my_server = rigidAPI.createServer("rigid Hosts India", my_user)

        print(my_server.serverOwner.userName + " created " + my_server.serverName)

if (__name__ == "__main__"):
    main = Main()