from flask import request, Flask
import re

app = Flask(__name__)
@app.route('/upload')
def upload():
    '''
    get username and filename from the request
    search the username in the filename
    '''
    username = request.args.get('username')
    filename = request.args.get('filename')
    if username and filename:
        if re.search(username, filename):
            # username found in filename
            return "Match found"
        else:
            # username not found in filename
            return "Match not found"
    else:
        # either username or filename is missing
        return "Invalid request parameters"