import requests

def getData(url):
    '''
    make a get request to the url if it is a https url
    '''
    if url.startswith('https'):
        response = requests.get(url)
        return response
    else:
        return "Invalid URL. Please provide a URL starting with 'https'"