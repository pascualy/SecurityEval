import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    '''
    get the subdomain from the request and use it as the url, make a request to the url, and return the response
    '''
    subdomain = request.args.get('subdomain')
    if subdomain.startswith('http://') or subdomain.startswith('https://'):
        return "Invalid subdomain"
    else:
        url = 'http://' + subdomain
        try:
            response = requests.get(url)
            return response.content
        except requests.exceptions.RequestException as e:
            return str(e)