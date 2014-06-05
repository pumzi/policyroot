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

