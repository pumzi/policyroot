# -*- coding: utf-8 -*-

# Section 1: Imports
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.mail import Mail

# Section 2: Initialize a Flask app object
app = Flask(__name__)
app.config.from_object('config')

# Section 3: Fire up the database
db = SQLAlchemy(app)

# Section 4: Turn on/initialize the mail tools
mail = Mail(app)


# Section 5: Start up the login manager that you've imported
lm = LoginManager()			# Create a login manager object
lm.init_app(app)			# Initialize the login manager for this application
lm.login_view = 'index'		# If the user tries to go to a protected page, where do I redirect them?


# Section 6: Once we've initialized our systems, now go get views and models
from app import views, models 
