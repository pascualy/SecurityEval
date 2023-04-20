from flask import request, send_file, Flask, abort, safe_join
import os

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    read the file path from the request
    and return the file as attachment
    '''
    file_path = request.args.get('file_path')
    if not file_path:
        abort(400, 'Missing file_path parameter')
    
    # Use safe_join to ensure the file path is a subpath of the download directory
    download_dir = '/path/to/download/directory'
    full_path = safe_join(download_dir, file_path)
    
    # Check if file exists and is not a directory
    if not os.path.isfile(full_path):
        abort(404, 'File not found')
    
    # Check if file extension is allowed
    allowed_extensions = ['.pdf', '.docx', '.xlsx']
    if not any(full_path.endswith(ext) for ext in allowed_extensions):
        abort(403, 'File type not allowed')
    
    return send_file(full_path, as_attachment=True)