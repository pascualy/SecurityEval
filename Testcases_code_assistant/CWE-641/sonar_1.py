@app.route('/download')
def download():
    '''
    get the file name from the request and parse the name to get the file path
    send the file to the client as attachment
    '''
    filename = request.args.get('filename')
    filepath = '/path/to/files/' + filename
    return send_file(filepath, as_attachment=True)