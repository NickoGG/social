from flask import Flask
from config import Config

apl = Flask(__name__)
apl.config.from_object(Config)

from app import routes