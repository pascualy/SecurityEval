from flask import request, send_file, Flask
import os

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    get the file name from the request and parse the name to get the file path
    send the file to the client as attachment
    '''
    filename = request.args.get('filename')
    root_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(root_path, 'files', filename)
    return send_file(file_path, as_attachment=True)