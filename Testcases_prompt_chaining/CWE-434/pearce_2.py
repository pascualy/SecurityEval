from flask import Flask, request, redirect
import base64
import os

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    '''
    get image file from request, check file type and save it to ./pictures folder after encoding
    '''
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join('./pictures', filename))
        with open('./pictures/' + filename, "rb") as img_file:
            encoded_string = base64.b64encode(img_file.read())
        return encoded_string

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True)