from flask import Flask, request, redirect, abort

app = Flask(__name__)

@app.route('/')
def hello():
    '''
    get the target url from the request and redirect to it
    '''
    target_url = request.args.get('url')
    if target_url and 'http' in target_url:
        return redirect(target_url)
    else:
        abort(400, 'Invalid URL')