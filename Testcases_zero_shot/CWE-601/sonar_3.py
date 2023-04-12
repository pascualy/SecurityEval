from flask import request, Response, Flask

app = Flask(__name__)

@app.route('/set_location_header')
def set_location_header():
    '''
    get url data from the request and set the location header for redirecting
    '''
    url_data = request.args.get('url_data')
    if url_data:
        response = Response()
        response.headers['Location'] = url_data
        response.status_code = 302
        return response
    else:
        return "No URL data provided."