from bson import ObjectId
from datetime import datetime, timezone
from src import mongo

class User:
    def __init__(self, fullName, userName, email, password):
        self.fullName = fullName
        self.userName = userName
        self.email = email
        self.password = password
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = datetime.now(timezone.utc)

    def save(self):
        mongo.db.users.insert_one({
            'fullName': self.fullName,
            'userName': self.userName,
            'email': self.email,
            'password': self.password,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        })

    @staticmethod
    def find(userName):
        return mongo.db.users.find_one({'userName': userName})
    
    @staticmethod
    def find_by_email(email):
        return mongo.db.users.find_one({'email': email})
    
    @staticmethod
    def find_by_id(user_id):
        user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
        if user:
            user['_id'] = str(user['_id'])  
        return user
    
    @staticmethod
    def find_all_user():
        return list(mongo.db.users.find())

    @staticmethod
    def find_by_id_and_update(user_id,update_data):
        update_data['updated_at'] = datetime.now(timezone.utc)
        mongo.db.users.update_one({'_id': ObjectId(user_id)}, {'$set': update_data})
    
    @staticmethod
    def find_by_id_and_delete(user_id):
        return mongo.db.users.find_one_and_delete({'_id': ObjectId(user_id)})