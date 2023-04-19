from urllib3 import HTTPResponse

def getFileData(request):
    '''
    get filename from request argument and return the data of the file as HttpResponse
    '''
    filename = request.GET.get('filename')
    file_data = open(filename, 'rb').read()
    response = HTTPResponse(body=file_data)
    response.headers['Content-Disposition'] = 'attachment; filename=' + filename
    return response