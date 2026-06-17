import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'pc-direct-downloader-secret-key-2026')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///software.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
