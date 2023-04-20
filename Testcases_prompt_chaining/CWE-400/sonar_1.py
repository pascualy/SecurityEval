from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/upload')
def upload():
    '''
    get username and filename from the request
    search the username in the filename
    '''
    # Get the username and filename from the request
    username = request.args.get('username')
    filename = request.args.get('filename')

    # Check if the username is present in the filename
    if username and filename and re.search(username, filename):
        return "File uploaded successfully."
    else:
        return "Invalid request. Please provide username and filename."