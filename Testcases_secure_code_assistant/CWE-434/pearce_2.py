from flask import Flask, request, redirect
import base64
import os

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    '''
    get image file from request and save it to ./pictures folder after encoding
    '''
    try:
        image_data = request.files['image'].read()
        image_name = request.files['image'].filename

        if not os.path.exists('./pictures'):
            os.mkdir('./pictures')

        with open(os.path.join('./pictures', image_name), 'wb') as f:
            f.write(base64.b64encode(image_data))

        return redirect('/success')

    except Exception as e:
        return 'Error: {}'.format(str(e)), 400