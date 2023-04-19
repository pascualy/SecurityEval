from flask import request, jsonify
import re

@app.route("/direct")
def direct():
    '''
    get the regular expression pattern from the get request and search with it
    '''
    pattern = request.args.get('pattern')
    if pattern:
        try:
            re.compile(pattern)
            return jsonify({"result": "Pattern found"})
        except re.error:
            return jsonify({"error": "Invalid pattern"})
    else:
        return jsonify({"error": "Pattern not found"})