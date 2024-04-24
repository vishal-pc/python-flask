from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from src.models.user import User
from src.config import Config
import jwt
import datetime


def register():
    fullName = request.json.get('fullName')
    userName = request.json.get('userName')
    email = request.json.get('email')
    password = generate_password_hash(request.json.get('password'))
    user = User(fullName, userName, email, password)
    user.save()
    return jsonify(message='User registered successfully'), 201


def login():
    email = request.json.get('email')
    password = request.json.get('password')
    user = User.find_by_email(email)
    if user and check_password_hash(user['password'], password):
        expiration_time = datetime.datetime.now(datetime.timezone.utc) + Config.JWT_ACCESS_TOKEN_EXPIRES
        token = jwt.encode(
            {'user_id': str(user['_id']),
             'fullName': user['fullName'],
             'userName': user['userName'],
             'email': user['email'],
             'exp': expiration_time}, 
            Config.JWT_SECRET_KEY,
            algorithm='HS256'
        )
        return jsonify(message='User login successfully', access_token=token), 200
    return jsonify(message='Invalid email or password'), 401

