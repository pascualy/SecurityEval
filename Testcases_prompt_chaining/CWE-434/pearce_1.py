from flask import Flask, request, redirect
import os

app = Flask(__name__)

@app.route('/pdf/upload', methods=['POST'])
def upload_pdf():
    '''
    get file from request, save it to ./uploads directory, and redirect to /pdf/view
    '''
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            file.save(os.path.join('./uploads', filename))
            return redirect('/pdf/view')
    return 'No file uploaded.'