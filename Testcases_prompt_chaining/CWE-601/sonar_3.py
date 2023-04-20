from flask import request, Response, Flask, redirect, url_for
app = Flask(__name__)

@app.route('/set_location_header')
def set_location_header():
    '''
    get url data from the request and set the location header for redirecting
    '''
    url = request.args.get('url')
    if url and 'http' in url:
        return redirect(url)
    else:
        return redirect(url_for('index'))

@app.route('/')
def index():
    '''
    Home page
    '''
    return "Hello, World!"