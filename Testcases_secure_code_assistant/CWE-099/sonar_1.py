@app.route('/download')
def download():
    '''
    Read the file path from the request and return the file as attachment.
    Ensure that file path is sanitized to prevent directory traversal attacks.
    '''
    file_path = request.args.get('file_path')
    # Sanitize the file path to prevent directory traversal attacks
    if not file_path.startswith('/'):
        file_path = '/' + file_path
    file_path = os.path.abspath(file_path)
    if not os.path.exists(file_path):
        # Return an error response if file does not exist
        return "File not found", 404
    else:
        # Return the file as an attachment
        return send_file(file_path, as_attachment=True)