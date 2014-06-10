# Section 1: Imports
from flask.ext.login import LoginManager


# Section 2: Database configuration stuff
SQLALCHEMY_DATABASE_URI = 'postgresql://aliya:Popcorn13@localhost/policyroot'


# Section 3: Configuring our forms tool
CSRF_ENABLED = True #This is to prevent CSRF attacks - so that all of our data comes from our forms
SECRET_KEY = 'big-secret'


# Section 4: Configuring our email tool
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'katherine@codeforprogress.org'
MAIL_PASSWORD = 'kathy1322'
ADMINS = ['katherine@codeforprogress.org', 'bobbyjoe@codeforprogress.org', 'dago@codeforprogress.org']