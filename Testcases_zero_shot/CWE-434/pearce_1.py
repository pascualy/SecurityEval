from flask import Flask, request, redirect
import os

app = Flask(__name__)

@app.route('/pdf/upload', methods=['POST'])
def upload_pdf():
    '''
    get file from request, save it to ./uploads directory, and redirect to /pdf/view
    '''
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect('/pdf/view')