class User:
    def __init__(self, username):
        self._username = username

    def role(self):
        return "User"

class Admin(User):
    def role(self):
        return "Admin"