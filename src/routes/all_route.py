from flask import Blueprint
from src.controllers.auth_controller import *
from src.controllers.user_controller import *
from src.middleware.verify_token import verify_token


auth_bp = Blueprint('api', __name__, url_prefix='/api')

# Auth Routes
@auth_bp.route('/register', methods=['POST'])
def register_route():
    return register()

@auth_bp.route('/login', methods=['POST'])
def login_route():
    return login()


# User Routes
@auth_bp.route('/user', methods=['GET'])
@verify_token
def get_user_by_id_route():
    user_id = request.user_id
    return getUserById(user_id)

@auth_bp.route('/users', methods=['GET'])
@verify_token
def get_all_user_route():
    return getAllUser()

@auth_bp.route('/user-update', methods=['PATCH'])
@verify_token
def update_user_by_id_route():
    user_id = request.user_id
    return updateUser(user_id)

@auth_bp.route('/user-delete', methods=['DELETE'])
@verify_token
def delete_user_by_id_route():
    user_id = request.user_id
    return deleteUser(user_id)