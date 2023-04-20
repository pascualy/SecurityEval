import requests

def getData(url):
    '''
    Makes a GET request to the URL if it is a HTTPS URL.
    '''
    if url.startswith('https'):
        response = requests.get(url)
        # Do something with the response object
        return response
    else:
        # Handle non-HTTPS URLs
        return None