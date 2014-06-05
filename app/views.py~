# -*- coding: utf-8 -*-

from app import app
from flask import render_template

@app.route('/')
def index():
	return render_template("RHMHome.html")


@app.route('/feedback')
def feedback():
	return render_template("RHMFeedback.html")

@app.route('/issues')
def issues():
	return render_template("RHMIssues.html")


@app.route('/worker')
def worker():
	return render_template("RHMWorker.html")