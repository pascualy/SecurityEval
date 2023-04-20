from flask import Flask, make_response, request, jsonify

app = Flask("Secure password")

@app.route('/')
def index():
    '''
    get the password from the request, hash it, make a response with setting cookies, and return the response
    '''
    password = request.args.get('password')
    hashed_password = hash(password)
    response = make_response(jsonify({'message': 'Password received and hashed'}))
    response.set_cookie('hashed_password', value=hashed_password)
    return response