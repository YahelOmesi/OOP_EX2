from User import User


class SocialNetwork:
    _instance = None

    def __new__(cls, name):  # Singleton design pattern
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    # self == this (סוג של)
    def __init__(self, name):
        self.name = name  # of the social network
        self._users = dict()  # map between username to user
        self._connected = set()  # save who is login
        print(f"The social network {name} was created!")

    def sign_up(self, username, password):
        if username in self._users:
            raise ValueError("username already taken")

        new_user = User(username, password)
        self._users[username] = new_user
        self._connected.add(username)
        return new_user

    def log_out(self, username):
        if username in self._connected:
            self._connected.remove(username)
            print(username + " disconnected")

    def log_in(self, username, password):
        if username in self._users:
            user = self._users[username]
            if user.get_password() == password:
                self._connected.add(username)
                print(username + " connected")

        else:
            raise ValueError("The username and password are not correct")

    def __str__(self):
        result = f"{self.name} social network:\n"
        for username, user in self._users.items():  # Iterate over the dictionary items
            result += str(user) + "\n"  # Concatenate the string representations of users
        return result
