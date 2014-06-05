# -*- coding: utf-8 -*-

from app import app, db
from flask import Flask, render_template, redirect
from models import Post, User
from forms import NewUserForm

@app.route('/')
def index():
	users = User.query.all()
	posts = Post.query.all()
	return render_template('index.html', users = users, posts = posts )

@app.route('/add_user', methods = ['GET', 'POST'])
def add_user():
	form = NewUserForm()
	if form.validate_on_submit():
		user = User()
		form.populate_obj(user)
		db.session.add(user)
		db.session.commit()
		return redirect('/')
	return render_template("add_user.html", form = form)
