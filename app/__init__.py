from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from app.config import Config

flask_app = Flask(__name__)
flask_app.config.from_object(Config)
db = SQLAlchemy(flask_app)
login_manager = LoginManager(flask_app)
login_manager.login_view="login"
migrate = Migrate(flask_app,db)


from app import routes
from app import models
