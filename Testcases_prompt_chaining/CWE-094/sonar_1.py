from flask import request
import urllib

@app.route('/')
def index():
    '''
    get the module version from the request
    importing the urllib module with the version using a safe method
    '''
    version = request.args.get('version')
    if version:
        module = __import__('urllib'+ version)
    else:
        module = urllib
    return "Module version: {}".format(module.__version__)