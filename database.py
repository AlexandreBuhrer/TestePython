import json

class Database:
    def __init__(self, filename='users.json'):
        self.filename = filename
        # Se o arquivo não existir, cria um com um dicionário vazio
        try:
            with open(self.filename, 'r') as file:
                self.users = json.load(file)
        except FileNotFoundError:
            self.users = {}

    def load_users(self):
        return self.users

    def save_user(self, username, password):
        self.users[username] = password
        self._save_to_file()

    def user_exists(self, username):
        return username in self.users

    def _save_to_file(self):
        with open(self.filename, 'w') as file:
            json.dump(self.users, file)
