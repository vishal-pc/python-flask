from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from src.models.user import User
from src.config import Config
import jwt
import datetime
from src.helper.helper import validate_email, validate_password


def register():
    fullName = request.json.get('fullName')
    userName = request.json.get('userName')
    email = request.json.get('email')
    password = request.json.get('password')

    # Check for missing fields
    if not fullName:
        return jsonify(message='Full Name is required'), 400
    elif not userName:
        return jsonify(message='User Name is required'), 400

    # Perform validation
    email_error = validate_email(email)
    password_error = validate_password(password)

    if email_error:
        return jsonify(message=email_error), 400
    elif password_error:
        return jsonify(message=password_error), 400
    
    # Check if email already exists in the database
    if User.find_by_email(email=email):
        return jsonify(message='Email already exists. Please use a different email.'), 400

    password = generate_password_hash(password)
    user = User(fullName, userName, email, password)
    user.save()
    return jsonify(message='User registered successfully'), 201


def login():
    email = request.json.get('email')
    password = request.json.get('password')

    # Check for missing fields
    if not email:
        return jsonify(message='Email is required'), 400
    elif not password:
        return jsonify(message='Password is required'), 400
    
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
        return jsonify(message='User login successfully', token=token), 200
    return jsonify(message='Invalid email or password'), 401

