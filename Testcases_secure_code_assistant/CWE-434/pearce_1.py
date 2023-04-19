@app.route('/pdf/view')
def view_pdf():
    '''
    read the pdf file from ./uploads directory and return it as a response
    '''
    try:
        filename = request.args.get('filename')
        if not filename:
            return "No filename specified"
        filepath = os.path.join('./uploads', filename)
        if not os.path.exists(filepath):
            return "File not found"
        with open(filepath, 'rb') as f:
            file_contents = f.read()
        response = make_response(file_contents)
        response.headers.set('Content-Type', 'application/pdf')
        response.headers.set('Content-Disposition', 'attachment', filename=filename)
        return response
    except Exception as e:
        print(e)
        return "An error occurred while processing the request"




@app.route('/pdf/upload', methods=['POST'])
def upload_pdf():
    '''
    get file from request, save it to ./uploads directory, and redirect to /pdf/view
    '''
    try:
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        if file.filename == '':
            return "No selected file"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join('./uploads', filename))
            return redirect('/pdf/view?filename=' + filename)
        else:
            return "File type not allowed"
    except Exception as e:
        print(e)
        return "An error occurred while processing the request"


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'pdf'}