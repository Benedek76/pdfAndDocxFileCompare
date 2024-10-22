import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123456789'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://<DB Username>:<Password>@localhost/compare'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
