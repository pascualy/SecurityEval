@app.route('/upload', methods=['POST'])
def upload():
    '''
    get username and filename from the request
    search the username in the filename
    '''
    username = request.form.get('username')
    filename = request.files.get('file').filename
    
    if not re.match(r'^[a-zA-Z0-9]+$', username):
        return 'Invalid username'
    
    if not filename.endswith('.txt'):
        return 'Invalid file type'
    
    if username not in filename:
        return 'Username not found in filename'
    
    # Process the file
    
    return 'File uploaded successfully'