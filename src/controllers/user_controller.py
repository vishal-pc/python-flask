from flask_mail import Message
from flask import request, jsonify
from src.models.user import User
from src.config import Config
import jwt
from werkzeug.security import generate_password_hash
from src.helper.helper import validate_password
from src import mail 


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


def forgetPassword():
    email = request.json.get('email')
    if not email:
        return jsonify(message='Email is required'), 400
    
    user = User.find_by_email(email)
    if user:
        token = jwt.encode({'user_id': str(user['_id'])}, Config.JWT_SECRET_KEY, algorithm='HS256')
        reset_url = f"http://192.168.1.129:8080/resetpassword?token={token}"
        
        # Send email with reset URL
        msg = Message('Reset Your Password', sender=Config.MAIL_USERNAME, recipients=[email])
        msg.body = f"Click the following link to reset your password: {reset_url}"
        mail.send(msg)
        
        return jsonify(message='Reset link sent to your email'), 200
    return jsonify(message='Email not found'), 404


def resetPassword():
    token = request.args.get('token')
    if not token:
        return jsonify(message='Token is required'), 400
    
    password = request.json.get('password')
    confirmPassword = request.json.get('confirmPassword')
    if not password or not confirmPassword:
        return jsonify(message='New password and confirm password are required'), 400
    
    try:
        decoded_token = jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=['HS256'])
        user_id = decoded_token.get('user_id')
        if not user_id:
            raise jwt.InvalidTokenError
        
        if password != confirmPassword:
            return jsonify(message='New password and confirm password do not match'), 400
        
        password_error = validate_password(password)
        if password_error:
            return jsonify(message=password_error), 400
        
        hashed_password = generate_password_hash(password)
        User.find_by_id_and_update(user_id, {'password': hashed_password})
        
        return jsonify(message='Password reset successfully'), 200
    except jwt.ExpiredSignatureError:
        return jsonify(message='Token has expired'), 401
    except jwt.InvalidTokenError:
        return jsonify(message='Invalid token'), 401