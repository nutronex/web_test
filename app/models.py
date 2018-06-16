from flask_sqlalchemy import SQLAlchemy

from app import db
from app import login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def get_user(id):
    return User.query.get(int(id))

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),index=True,unique=True)
    email = db.Column(db.String(120),index = True, unique =True)
    password = db.Column(db.String(128))
    posts = db.relationship("Post",backref="user",lazy="dynamic")

    def set_password(self,passwd):
        self.password = generate_password_hash(passwd)

    def check_password(self,passwd):
        return check_password_hash(self.password,passwd)

    def __str__(self):
        return self.username


class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(150))
    timestamp = db.Column(db.DateTime,index=True,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"))
    def __str__(self):
        return self.title

