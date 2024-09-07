# authenticator.py

from database import Database

class Authenticator:
    def __init__(self):
        self.db = Database()
    
    def authenticate(self, username, password):
        users = self.db.load_users()
        return users.get(username) == password
    
    def register(self, username, password):
        if self.db.user_exists(username):
            return "User already exists."
        self.db.save_user(username, password)
        return "User registered successfully."
