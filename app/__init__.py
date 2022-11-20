import logging
from logging.handlers import SMTPHandler
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

if not apl.debug:
    if apl.config['MAIL_SERVER']:
        auth = None
        if apl.config['MAIL_USERNAME'] or apl.config['MAIL_PASSWORD']:
            auth = (apl.config['MAIL_USERNAME'], apl.config['MAIL_PASSWORD'])
        secure = None
        if apl.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(apl.config['MAIL_SERVER'], apl.config['MAIL_PORT']),
            fromaddr='no-reply@' + apl.config['MAIL_SERVER'],
            toaddrs=apl.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        apl.logger.addHandler(mail_handler)

from app import routes, errors, models