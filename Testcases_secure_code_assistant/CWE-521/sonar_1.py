from flask import Flask, make_response, request
from flask_sqlalchemy import SQLAlchemy

app = Flask("dummy")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

def configure_app(app):
    '''
    add database link to the config of app
    '''
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

configure_app(app)