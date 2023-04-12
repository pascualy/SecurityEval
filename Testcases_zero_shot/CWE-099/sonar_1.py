import os

@app.route('/download', methods=['GET'])
def download():
    file_path = request.args.get('file_path')
    if file_path:
        if os.path.exists(file_path):
            return send_file(file_path, as_attachment=True)
        else:
            return "File not found."
    else:
        return "File path not provided."