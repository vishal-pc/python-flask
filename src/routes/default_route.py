from flask import Blueprint

default_bp = Blueprint('default', __name__)

@default_bp.route('/', methods=['GET'])
def hello():
    return ('Hello from Flask')
