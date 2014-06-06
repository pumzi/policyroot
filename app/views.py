# -*- coding: utf-8 -*-
from app import app, db#, lm
from flask import render_template, redirect
from flask.ext.login import login_user, logout_user, login_required
from models import Post, User
from forms import NewUserForm, LoginForm, NewPostForm
from emails import follower_notification

@app.route('/')
@login_required
def index():
  	form = LoginForm()
	if form.validate_on_submit():
		user = form.get_user()
		login_user(user)
		return redirect('/')
	return render_template('index.html', form = form)

@app.route('/sign_up', methods = ['GET', 'POST'])
def sign_up():
<<<<<<< HEAD
	form = NewUserForm()
	if form.validate_on_submit():
		user = User()
		form.populate_obj(user)
		db.session.add(user)
		db.session.commit()
		return redirect('/')
	return render_template('sign_up.html', form = form)
=======
	form = NewUserForm()			#calling on NewUserForm from forms.py
	if form.validate_on_submit():	#if statement: saying the if the submit button is pushed then,
		user = User() 				#it prepares a new row for the info to be passed in
		form.populate_obj(user)		#then populates new user info entered by user
		db.session.add(user)		#creates the new user 
		db.session.commit()			#then commits and saves to the database
		return redirect('/')		#after it is submitted, it redirects to...
	return render_template('.html', form = form) # the topics page
>>>>>>> 9650b813e10ff9da1398f85b29f69bdf2b55b149

@app.route('/topics')
def topics():						#This is the topics page that has hyperlinks to each subtopic
	return render_template('topics.html')

@app.route('/Undocuqueer', methods = ['GET', 'POST'])
def Undocuqueer():
	form = NewPostForm(Form)		#calling on NewPostForm from forms.py
	if form.validate_on_submit():	#if statement: saying the if the submit button is pushed then,
		post = Post()				#it prepares a new row for the info to be passed in
		form.populate_obj(post)		#then populates new post info entered by user
		db.session.add(post)		#creates new post 
		db.session.commit()			#after it is submitted, it redirects back to the,
		return redirect('/Undocuqueer') #Undocuqueer page 
	users = User.query.all				#This GETs users to show on the page
	posts = Post.query.filter_by(topic='Undocuqueer') #with post filtered by the topic
	return render_template('Undocuqueer.html', form = form, users = users, posts = posts)

@app.route('/pathway', methods = ['GET', 'POST'])
def pathway():
	form = NewPostForm(Form)
	if form.validate_on_submit():
		post = Post()
		form.populate_obj(post)
		db.session.add(post)
		db.session.commit()
		return redirect('/pathway')
	users = User.query.all
	posts = Post.query.filter_by(topic='pathway')
	return render_template('pathway.html', form = form, users = users, posts = posts)

@app.route('/know_your_rights', methods = ['GET', 'POST'])
def know_your_rights():
	form = NewPostForm(Form)
	if form.validate_on_submit():
		post = Post()
		form.populate_obj(post)
		db.session.add(post)
		db.session.commit()
		return redirect('/know_your_rights')
	users = User.query.all
	posts = Post.query.filter_by(topic= 'know_your_rights')
	return render_template('know_your_rights.html', form = form, users = users, posts = posts)

@app.route('/colonialism', methods = ['GET', 'POST'])
def colonialism():
	form = NewPostForm(Form)
	if form.validate_on_submit():
		post = Post()
		form.populate_obj(post)
		db.session.add(post)
		db.session.commit()
		return redirect('/colonialism')
	users = User.query.all
	posts = Post.query.filter_by(topic = 'colonialism')
	return render_template('colonialism.html', form = form, users = users, posts = posts)

@app.route('/follow/<nickname>')
@login_required
def follow(nickname):
    user = User.query.filter_by(nickname = nickname).first()
    # ...
    follower_notification(user, g.user)
    return redirect(url_for('user', nickname = nickname))

