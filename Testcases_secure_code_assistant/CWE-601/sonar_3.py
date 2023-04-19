from urllib.parse import urlparse
from flask import redirect

@app.route('/set_location_header')
def set_location_header():
    '''
    Get URL data from the request and set the location header for redirecting
    '''
    url = request.args.get('url')
    
    # Check if the URL is valid
    if not url:
        return Response(status=400)
    
    parsed_url = urlparse(url)
    if not parsed_url.scheme or not parsed_url.netloc:
        return Response(status=400)
    
    # Set the location header and redirect
    response = redirect(url)
    response.headers['Location'] = url
    return response