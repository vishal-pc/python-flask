from bson import ObjectId
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


def updateUser(user_id):
    user_data = request.json

    user = User.find_by_id(user_id)
    if not user:
        return jsonify(message='User not found'), 404

    if 'fullName' in user_data:
        user['fullName'] = user_data['fullName']
    if 'userName' in user_data:
        user['userName'] = user_data['userName']

    update_data = {key: value for key, value in user.items() if key != '_id'}

    User.find_by_id_and_update(user_id, update_data)

    return jsonify(message='User updated successfully'), 200


def deleteUser(user_id):
    user = User.find_by_id_and_delete(user_id)
    if not user:
        return jsonify(message='User not found'), 404
    return jsonify(message='User deleted successfully'), 200