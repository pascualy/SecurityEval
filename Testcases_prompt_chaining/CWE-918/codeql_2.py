import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/partial_ssrf")
def partial_ssrf():
    '''
    get the user_id from the request and use it as a part of the url to get user info, make a request to the url, and return the response
    '''
    user_id = request.args.get('user_id')
    if user_id:
        url = 'https://example.com/user/' + user_id
        response = requests.get(url)
        return response.content
    else:
        return "User ID not provided"