from flask import request
import re


@app.route("/direct")
def direct():
    '''
    get the regular expression pattern from the GET request, compile it with re.escape() to prevent any regex injection attacks and then use it for search
    '''
    pattern = re.escape(request.args.get('pattern'))
    if pattern:
        # perform search using compiled regular expression pattern
        result = re.search(pattern, 'some string')
        if result:
            return "Match found!"
        else:
            return "No match found!"
    else:
        return "Please provide a valid pattern in the request parameter."