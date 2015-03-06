from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from blog import app
import hashlib

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80),unique=True)
	email = db.Column(db.String(160),unique=True)
	password = db.Column (db.String(256),unique=False)

	def __init__(self,username,email,password):
		self.username = username
		self.email = email
		self.password = password

	def __repr__(self):
		return '<User %r>' % self.username