# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


from app import views, models 

from flask.ext.mail import Mail
mail = Mail(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'



