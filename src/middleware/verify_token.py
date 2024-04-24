from functools import wraps
import jwt
from flask import request, jsonify
from src.config import Config

def get_user_id_from_token():
    token = None
    if "Authorization" in request.headers:
        token = request.headers["Authorization"].split(" ")[1]
    if not token:
        return None
    try:
        data = jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=["HS256"])
        user_id = data.get("user_id")
        return user_id
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
    except Exception:
        return None

def verify_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        user_id = get_user_id_from_token()
        if not user_id:
            return jsonify({
                "message": "Invalid Authentication token!",
                "data": None,
                "error": "Unauthorized"
            }), 401
        request.user_id = user_id  
        return f(*args, **kwargs)
    return decorated
