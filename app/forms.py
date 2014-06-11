from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, PasswordField
from wtforms.validators import Required 

from models import User

class NewUserForm(Form):
	firstname = TextField('firstname')
	lastname = TextField('lastname')
	second_lastname = TextField('second_lastname')
	username = TextField('username', validators= [Required(message = 'We need your username!')])
	email = TextField('email', validators= [Required(message= 'We need a valid email')])
	password = TextField('password')
	role = TextField('role')
	location = TextField('location')

class NewPostForm(Form):
	title = TextField('title')
	author = TextField('author')
	topic = TextField('topic')
	content = TextAreaField('content')

class LoginForm(Form):
	email = TextField('email', validators = [Required(message="We need to know your email address.")])
	password = PasswordField('password', validators = [Required(message="We need your password.")])

	def get_user(self):
		return User.query.filter_by(email=self.email.data).first()