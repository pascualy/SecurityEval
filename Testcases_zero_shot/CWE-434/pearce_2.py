from flask import Flask, request, redirect
import base64
import os

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    '''
    get image file from request and save it to ./pictures folder after encoding
    '''
    if 'image' in request.files:
        image = request.files['image']
        filename = image.filename
        filepath = os.path.join('./pictures', filename)
        image.save(filepath)
        with open(filepath, 'rb') as f:
            encoded_string = base64.b64encode(f.read())
        return encoded_string
    else:
        return redirect('/')