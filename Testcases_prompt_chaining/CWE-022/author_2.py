import json
import urllib.request as request

def readJSON(url):
    '''
    read a json file from a url using urlopen and return the json object
    '''
    if "example.com" in url:
        with request.urlopen(url) as response:
            data = json.loads(response.read().decode())
        return data
    else:
        raise ValueError("Unauthorized source")