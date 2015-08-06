from flask import Flask

api = Flask(__name__)
api.debug = True

__version__ = '0.1.0'

from app import routes
