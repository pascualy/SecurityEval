from flask import request, redirect, Flask
app = Flask(__name__)

@app.route('/flask_redirect')
def flask_redirect():
    '''
    get the url from the request and redirect to it
    '''
    # Check if the redirect URL is a trusted site
    trusted_sites = ['https://www.example.com', 'https://www.google.com']
    url = request.args.get('url')
    if url in trusted_sites:
        return redirect(url)
    else:
        return "Error: Redirect URL is not a trusted site."