import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'Fliph106')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://Fliph106@localhost/login/api')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'Fliph106')