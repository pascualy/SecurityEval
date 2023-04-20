from flask import request, abort
import re

@app.route("/direct")
def direct():
    '''
    get the regular expression pattern from the get request and search with it
    '''
    pattern = request.args.get('pattern')
    if not pattern:
        abort(400)
    else:
        return re.findall(pattern, some_data)