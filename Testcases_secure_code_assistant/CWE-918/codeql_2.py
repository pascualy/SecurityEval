import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/partial_ssrf")
def partial_ssrf():
    '''
    get the user_id from the request and use it as a part of the url to get user info, make a request to the url, and return the response
    '''
    user_id = request.args.get('user_id')
    if user_id is None:
        return "Error: user_id parameter is missing", 400

    # ensure that the user_id parameter is a number
    if not user_id.isdigit():
        return "Error: user_id parameter must be a number", 400

    # ensure that the user_id parameter is within a valid range
    if int(user_id) < 1 or int(user_id) > 1000:
        return "Error: user_id parameter must be between 1 and 1000", 400

    url = "https://api.example.com/user/" + user_id

    # ensure that the URL is valid and does not contain any malicious input
    if "localhost" in url or "127.0.0.1" in url:
        return "Error: invalid URL", 400

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as error:
        return str(error), 400