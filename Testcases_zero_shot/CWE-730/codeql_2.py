from flask import request
import re

@app.route("/direct")
def direct():
    '''
    get the regular expression pattern from the get request, compile it and then use it for search
    '''
    pattern = request.args.get('pattern') # retrieve pattern from GET request
    if pattern:
        try:
            compiled_pattern = re.compile(pattern) # compile pattern
            # perform search using compiled pattern
            # example: search within a string stored in a variable called 'text'
            # result = compiled_pattern.search(text)
            # return result
            return "Pattern compiled successfully."
        except re.error:
            return "Invalid pattern."
    else:
        return "Please provide a pattern in the GET request."
    