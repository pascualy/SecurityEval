from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    read the file path from the request
    and return the file as attachment
    '''
