import json
import urllib.request as request

def readJSON(url):
    '''
    read a json file from a url using urlopen and return the json object
    '''
    with request.urlopen(url) as response:
        data = response.read()
        json_obj = json.loads(data.decode('utf-8'))
    return json_obj