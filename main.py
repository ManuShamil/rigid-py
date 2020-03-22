from rigidMaster import API

class Main:
    def __init__(self):

        rigidAPI = API()

        my_user = rigidAPI.createUser("manu_shamil","manusshamil@gmail.com")

if (__name__ == "__main__"):
    main = Main()