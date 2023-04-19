from pathlib import Path

@app.route('/download')
def download():
    try:
        filename = request.args.get('filename')
        if not filename:
            return "Filename not specified", 400

        # Check if the file exists and is not a directory
        file_path = Path(filename)
        if not file_path.is_file():
            return "File not found", 404

        # Check if the file is within the allowed directory
        if not file_path.resolve().parent == Path('/path/to/allowed/directory').resolve():
            return "File access denied", 403

        return send_file(file_path, as_attachment=True)

    except Exception as e:
        # Log the error and return an error message to the client
        app.logger.error(f"Error while downloading file: {e}")
        return "Error while downloading file", 500