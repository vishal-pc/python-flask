from flask import Flask
from flask_pymongo import PyMongo
from src.config import Config
from flask_mail import Mail


app = Flask(__name__)
app.config.from_object(Config)
mongo = PyMongo(app)
mail = Mail(app)

# Check MongoDB connection
try:
    mongo.db.command('ping')
    print("Database Connected...👍️")
except Exception as e:
    print("Database not connected...🥱", e)

# Import routes after initializing app to avoid circular imports
from src import routes
