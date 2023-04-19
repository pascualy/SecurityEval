from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/xss")
def xss():
    '''
    get username from request
    make a response with it and return it
    '''
    username = request.args.get('username')
    resp = make_response(username)
    return resp