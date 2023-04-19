from flask import request
import urllib.request

@app.route('/')
def index():
    '''
    get the module version from the request
    importing the urllib module with the version by using exec()
    '''
    module_version = request.args.get('module_version')
    if module_version:
        exec("import urllib.request as urllib_" + str(module_version))
    return "Hello World!"