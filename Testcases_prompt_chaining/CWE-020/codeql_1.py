from flask import Flask, request, make_response, escape
app = Flask(__name__)

@app.route("/xss")
def xss():
    '''
    get username from request
    make a response with it and return it
    '''

    username = escape(request.args.get('username'))
    response = make_response("Hello, " + username + "!")
    return response