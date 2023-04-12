filename = request.args.get('filename')
filepath = '/path/to/files/' + filename
return send_file(filepath, as_attachment=True)