from datetime import timedelta
import os
from dotenv import load_dotenv # type: ignore

# Load environment variables from .env file
load_dotenv()

class Config:
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    MONGO_URI = os.getenv('MONGO_URI')
    PORT = os.getenv('PORT')
