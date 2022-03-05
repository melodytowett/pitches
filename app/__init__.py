from ensurepip import bootstrap
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
from app.main import routes
from flask_bootstrap import Bootstrap


bootstrap = Bootstrap()
db = SQLAlchemy()