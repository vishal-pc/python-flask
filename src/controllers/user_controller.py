from flask import request, jsonify
from src.models.user import User



def getUserById(user_id):
    user = User.find_by_id(user_id)
    if user:
        user.pop('password', None)
        return jsonify(user), 302
    else:
        return jsonify(message='User not found'), 404



def getAllUser():
    users = User.find_all_user()
    for user in users:
        user['_id'] = str(user['_id'])
    return jsonify(users), 302
