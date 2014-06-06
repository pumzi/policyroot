import os
basedir = os.path.abspath(os.path.dirname(__file__)) 


SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/policyroot'

from flask.ext.login import LoginManager
from config import basedir

lm = LoginManager()

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/swamperdb'

#We need the login for the postres sql 

CSRF_ENABLED = True #This is to prevent CSRF attacks - so that all of our data comes from our forms
SECRET_KEY = 'big-secret'
