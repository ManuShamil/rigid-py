from .api import User

    
class API:
    def __init__(self):
        print("rigid Master API")

    def createUser(self, name, email):
        """Registers a new user to database
        
        Arguments:
            name {str} -- User name of the user
            email {str} -- Email of the user
        
        Returns:
            User -- Authorized User Object
        """

        user = User(name, email)
        user.register()

        return user

    def loginUser(self, name, email):
        """Logs in user
        
        Arguments:
            name {str} -- User name of the user
            email {str} -- Email of the user
        
        Returns:
            User -- Authorized User Object
        """

        user = User(name, email)
        user.login()

        return user