import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin123@localhost:5432/bloG_weB'
    SQLALCHEMY_TRACK_MODIFICATIONS = False       
