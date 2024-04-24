from flask import request, jsonify
from flask_jwt_extended import create_access_token, JWTManager
from werkzeug.security import generate_password_hash, check_password_hash
from src.models.user import User


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
        access_token = create_access_token(identity=str(user['_id']), 
                                           additional_claims={
                                                              'user_id': str(user['_id']),
                                                              'fullName': user['fullName'],
                                                              'userName': user['userName'],
                                                              'email': user['email'],
                                                              })  
        return jsonify(message='User login successfully', access_token=access_token), 200
    return jsonify(message='Invalid email or password'), 401
