import requests

def getData(url):
    '''
    make a get request to the url if it is a https url
    '''
    if url.startswith('https://'):
        response = requests.get(url)
        return response.text
    else:
        return "Error: Only HTTPS urls are allowed."