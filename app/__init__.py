from ensurepip import bootstrap
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from app.main import routes
from flask_bootstrap import Bootstrap

def create_app(config_name):
    app = Flask(__name__)

    bootstrap = Bootstrap()
    db = SQLAlchemy()

    bootstrap.init_app(app)
    db.init_app(app)