# -*- coding: utf-8 -*-
from app import app
from flask import render_template

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/sign_up')
def sign_up():
	return render_template('sign_up.html')

@app.route('/topics')
def topics():
	return render_template('topics.html')

@app.route('/Undocuqueer')
def Undocuqueer():
	return render_template('Undocuqueer.html')

@app.route('/pathway')
def pathway():
	return render_template('pathway.html')

@app.route('/know_your_rights')
def know_your_rights():
	return render_template('know_your_rights.html')
@app.route('/colonialism')
def colonialism():
	return render_template('colonialism.html')

#=======

#from app import app, db
#from flask import Flask, render_template, redirect
#from models import Post, User
#from forms import NewUserForm

#@app.route('/')
#def index():
#	users = User.query.all()
#	posts = Post.query.all()
#	return render_template('index.html', users = users, posts = posts )

#@app.route('/add_user', methods = ['GET', 'POST'])
#def add_user():
#	form = NewUserForm()
#	if form.validate_on_submit():
#		user = User()
#		form.populate_obj(user)
#		db.session.add(user)
#		db.session.commit()
#		return redirect('/')
#	return render_template("add_user.html", form = form)
#>>>>>>> bbac8ee1b436ab8737ec10acf5da017000df2890
