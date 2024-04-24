from src import mongo

class User:
    def __init__(self, fullName, userName, email, password):
        self.fullName = fullName
        self.userName = userName
        self.email = email
        self.password = password

    def save(self):
        mongo.db.users.insert_one({
            'fullName': self.fullName,
            'userName': self.userName,
            'email': self.email,
            'password': self.password
        })

    @staticmethod
    def find(userName):
        return mongo.db.users.find_one({'userName': userName})
    
    @staticmethod
    def find_by_id(user_id):
        return mongo.db.users.find_one({'_id': user_id})
    
    @staticmethod
    def find_by_email(email):
        return mongo.db.users.find_one({'email': email})
