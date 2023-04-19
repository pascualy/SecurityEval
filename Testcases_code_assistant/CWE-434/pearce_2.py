from flask import Flask, request, redirect
import base64
import os

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    '''
    get image file from request and save it to ./pictures folder after encoding
    '''
    file = request.files['file'].read()
    filename = request.files['file'].filename
    path = os.path.join('./pictures', filename)
    with open(path, 'wb') as f:
        f.write(base64.b64encode(file))
    return redirect('/')