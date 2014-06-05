from app import db

class User(db.Model): #When you are making a new class you capitialize the title ex. class User()
	id = db.Column(db.Integer, primary_key = True)
	firstname = db.Column(db.String(100))
	lastname = db.Column(db.String(100))
	username = db.Column(db.String(120), unique =True)
	post = db.relationship('Post', backref = 'author')

class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String (100))
	content = db.Column(db.Text)
	author_id = db.Column(db.Integer, db.ForeignKey('user.id')) #when you are refering to a class, it is lowercase
