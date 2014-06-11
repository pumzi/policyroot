from app import db

class User(db.Model): #When you are making a new class you capitialize the title ex. class User() #still need to finish
	id = db.Column(db.Integer, primary_key = True)
	firstname = db.Column(db.String(100))
	lastname = db.Column(db.String(100))
	second_lastname = db.Column(db.String(100))
	username = db.Column(db.String(120), unique =True)
	email = db.Column(db.String(50))
	password = db.Column(db.String(12))
	role = db.Column(db.String(100))
	location = db.Column(db.String(100))
	post = db.relationship('Post', backref = 'activist') 

	def is_active(self):
		return True 
	def get_id(self):
		return self.id
	def is_authenticated(self):
		return True
	def is_anonymous(self):
		return False


class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(150))
	author = db.Column(db.String(100))
	topic = db.Column(db.String(100))
	content = db.Column(db.Text)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #when you are refering to a class, it is lowercase


