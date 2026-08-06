# Using json and file handling to create a simple login system in which user data will be stored in a json file
# and the user can register and login using the stored data.
'''


import json
import os


class LoginSystem:

    def __init__(self, file_name="users.json"):
        self.DATA_FILE = file_name

    def _load_users(self):
        if not os.path.exists(self.DATA_FILE):
            return []

        with open(self.DATA_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []

    def _save_users(self, users):
        with open(self.DATA_FILE, "w") as file:
            json.dump(users, file)

    def register_user(self, username, password):
        users = self._load_users()

        # Duplicate username check
        for user in users:
            if user["username"] == username:
                print("Username already exists!")
                return

        users.append({"username": username, "password": password})
        self._save_users(users)
        print(f"User {username} registered successfully.")

    def login_user(self, username, password):
        users = self._load_users()

        for user in users:
            if user["username"] == username and user["password"] == password:
                print("Login successful!")
                return True

        print("Invalid username or password.")
        return False


# Driver Code
if __name__ == "__main__":
    system = LoginSystem()

    system.register_user("john_doe", "password123")
    system.login_user("john_doe", "password123")
    system.login_user("john_doe", "wrongpassword")
'''

import json
import os

DATA_FILE = "Users.json"

def _load_users():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE,"r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def Save_user(user):
    with open(DATA_FILE,"w") as file:
        json.dump(user,file)
        
def resgister_user(userName,userPassword):
    Users = _load_users()
    for user in Users:
            if user["UserName"] == userName:
                print("Username already exists!")
                return
    Users.append({"UserName":userName,"Password":userPassword})
    Save_user(Users)

def Login(userName,userPassword):
    Users = _load_users()
    for User in Users:
        if(User["UserName"] == userName and User["Password"] == userPassword):
            print("Logged in success fully")
            return
    print("Invalid users")
    return

resgister_user("Monty","19Feb2004")
resgister_user("Ayush","01Nov2009")
Login("Monty","19Feb2004")
Login("Monty","19Feb2005")

    
