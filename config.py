import os
basedir = os.path.abspath(os.path.dirname(__file__)) 

<<<<<<< HEAD
#<<<<<<< HEAD
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/policyroot'
#=======
=======
<<<<<<< HEAD
#SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/policyroot'
=======

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/policyroot'

>>>>>>> 6017c718b7793d4ab3322f3d25fa68119177e345
from flask.ext.login import LoginManager
from config import basedir

lm = LoginManager()

<<<<<<< HEAD

#>>>>>>> f1f46c835d9d407cd475f1f3004fd0907d1f2062
=======
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/swamperdb'

>>>>>>> 3cafd111f342e82a825bcb1560ce7325de0a501e
>>>>>>> 6017c718b7793d4ab3322f3d25fa68119177e345
#We need the login for the postres sql 

CSRF_ENABLED = True #This is to prevent CSRF attacks - so that all of our data comes from our forms
SECRET_KEY = 'big-secret'
<<<<<<< HEAD

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'katherine@codeforprogress.org'
MAIL_PASSWORD = 'kathy1322'


ADMINS = ['katherine@codeforprogress.org', 'bobbyjoe@codeforprogress.org', 'dago@codeforprogress.org']
=======
>>>>>>> 3cafd111f342e82a825bcb1560ce7325de0a501e
