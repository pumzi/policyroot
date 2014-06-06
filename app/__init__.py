# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

<<<<<<< HEAD
from app import views, models 

from flask.ext.mail import Mail
mail = Mail(app)
=======
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

from app import views, models 
>>>>>>> 3cafd111f342e82a825bcb1560ce7325de0a501e
