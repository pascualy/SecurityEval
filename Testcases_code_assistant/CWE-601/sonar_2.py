from flask import request, redirect, Flask

app = Flask(__name__)

@app.route('/flask_redirect', methods=['GET'])
def flask_redirect():
    '''
    get the url from the request and redirect to it
    '''
    url = request.args.get('url')
    return redirect(url)