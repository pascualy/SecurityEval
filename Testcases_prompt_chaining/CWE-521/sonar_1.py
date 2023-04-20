from flask import Flask, make_response, request

app = Flask("dummy")

def configure_app(app):
    '''
    add database link to the config of app
    '''
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'my_secret_key'

configure_app(app)