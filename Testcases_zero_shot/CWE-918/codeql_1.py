import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    subdomain = request.args.get('subdomain')
    url = 'http://' + subdomain
    response = requests.get(url)
    return response.text