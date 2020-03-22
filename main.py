from rigidMaster import API

class Main:
    def __init__(self):

        rigidAPI = API()

        my_user = rigidAPI.createUser("rigid_user","rigid_user@rigid.com")

if (__name__ == "__main__"):
    main = Main()