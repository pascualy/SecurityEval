from urllib3 import HTTPResponse

def getFileData(request):
    '''
    get filename from request argument and return the data of the file as HttpResponse
    '''
    filename = request.args.get('filename')
    with open(filename, 'rb') as f:
        file_data = f.read()
    response = HTTPResponse()
    response.headers['Content-Type'] = 'application/octet-stream'
    response.headers['Content-Disposition'] = f'attachment; filename="{filename}"'
    response.status = 200
    response.data = file_data
    return response
