import os

base_dir = os.path.abspath( os.path.dirname(__file__))


class Config:
    SECRET_KEY = "FOOBAR"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(base_dir,"mydatabase.db")
    SQLALCHEMY_TRACK_MODIFICATIONS=False
