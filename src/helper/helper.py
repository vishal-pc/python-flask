import re

def validate_email(email):
    if not email:
        return "Email is required"
    elif not re.match(r'^[A-Za-z0-9._%-]+@(?:[A-Za-z0-9]+\.)+(com|co\.in|yahoo\.com)$', str(email)):
        return "Invalid email format"

def validate_password(password):
    if not password:
        return "Password is required"
    elif not re.match(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$', password):
        return "Password must have at least 8 characters, including at least one uppercase letter, one lowercase letter, one digit, and one special character (#?!@$%^&*-)"
