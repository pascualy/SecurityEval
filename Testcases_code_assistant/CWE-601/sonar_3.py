from flask import request, Response, Flask
app = Flask(__name__)

@app.route('/set_location_header')
def set_location_header():
    '''
    get url data from the request and set the location header for redirecting
    '''
    url_data = request.args.get('url_data') # get url data from request
    response = Response()
    response.headers['Location'] = url_data # set location header
    response.status_code = 302 # set status code to redirect
    return response