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
    if re.search(username, filename):
        # username found in filename
        return "File uploaded successfully"
    else:
        # username not found in filename
        return "Error: Username not found in filename"