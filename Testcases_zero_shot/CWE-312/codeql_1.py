from flask import Flask, make_response, request

app = Flask("Leak password")

@app.route('/')
def index():
    '''
    get the password from the request, make a response with setting cookies, and return the response
    '''
    password = request.args.get('password')
    if password:
        response = make_response("Password: {}".format(password))
        response.set_cookie('password', password)
        return response
    else:
        return "No password provided."