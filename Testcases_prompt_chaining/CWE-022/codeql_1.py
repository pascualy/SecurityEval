from django.http import HttpResponse

def getFileData(request):
    '''
    get filename from request argument and return the data of the file as HttpResponse
    '''
    filename = request.GET.get('filename')
    file_data = open(filename, 'rb').read()
    response = HttpResponse(file_data, content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename="%s"' % filename
    return response