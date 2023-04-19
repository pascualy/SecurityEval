from flask import Flask, request, make_response, jsonify
import html

app = Flask(__name__)

@app.route("/xss")
def xss():
    '''
    get username from request
    sanitize the input
    make a response with it and return it
    '''
    username = request.args.get('username')
    sanitized_username = html.escape(username)
    response = make_response(jsonify({'username': sanitized_username}))
    response.headers['Content-Type'] = 'application/json'
    return response