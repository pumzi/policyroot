# -*- coding: utf-8 -*-
from app import app, db #, lm
from flask import render_template, redirect
from flask.ext.login import login_user 
from models import Post, User
from forms import NewUserForm, LoginForm
from emails import follower_notification

@app.route('/')
def index():
  	form = LoginForm()
	if form.validate_on_submit():
		user = form.get_user()
		login_user(user)
		return redirect('/')
	return render_template('index.html', form = form)

@app.route('/sign_up', methods = ['GET', 'POST'])
def sign_up():
	form = NewUserForm()
	if form.validate_on_submit():
		user = User()
		form.populate_obj(user)
		db.session.add(user)
		db.session.commit()
		return redirect('/')
	return render_template('sign_up.html')

@app.route('/topics', methods = ['GET', 'POST'])
def topics():
	return render_template('topics.html')

@app.route('/Undocuqueer', methods = ['GET', 'POST'])
def Undocuqueer():
	#users = User.query.all()
	#posts = Post.query.all()
	return render_template('Undocuqueer.html')#, users = users, posts = posts)

@app.route('/pathway', methods = ['GET', 'POST'])
def pathway():
	#users = User.query.all()
	#posts = Post.query.all()
	return render_template('pathway.html')#, users = users, posts = posts)

@app.route('/know_your_rights', methods = ['GET', 'POST'])
def know_your_rights():
	#users = User.query.all()
	#posts = Post.query.all()
	return render_template('know_your_rights.html')#, users = users, posts = posts)

@app.route('/colonialism', methods = ['GET', 'POST'])
def colonialism():
	#users = User.query.all()
	#posts = Post.query.all()
	return render_template('colonialism.html')#, users = users, posts = posts)


@app.route('/follow/<nickname>')
@login_required
def follow(nickname):
    user = User.query.filter_by(nickname = nickname).first()
    # ...
    follower_notification(user, g.user)
    return redirect(url_for('user', nickname = nickname))

