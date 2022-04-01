from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

apl = Flask(__name__)
apl.config.from_object(Config)
db = SQLAlchemy(apl)
migrate = Migrate(apl, db)
login = LoginManager(apl)
login.login_view = 'login'

from app import routes, models