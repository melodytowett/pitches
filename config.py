from distutils.debug import DEBUG
import os

class Config():
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://melo:1234@localhost/pitches'

class ProdConfig(Config):

    pass

class DevConfig(Config):

    DEBUG = True