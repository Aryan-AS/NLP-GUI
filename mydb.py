import json
import os

class Database:
    def add_data(self, name, email, password):
        # Check if the file exists and is not empty
        if not os.path.exists("db.json") or os.stat("db.json").st_size == 0:
            database = {}  # If the file is empty, start with an empty dictionary
        else:
            with open("db.json", "r") as rf:
                database = json.load(rf)  # Load existing data

        if email in database:
            return 0
        else:
            database[email] = [name, password]
            with open("db.json", "w") as wf:
                json.dump(database, wf)
            return 1
    def search(self,email,password):
        with open("db.json","r") as rf:
            database = json.load(rf)
            if email in database:
                if database[email][1]== password:
                    return 1
                else:
                    return 0
                
            else:
                return 0
