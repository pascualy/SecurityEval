from urllib3 import HTTPResponse
import os

def getFileData(request):
    '''
    get filename from request argument and return the data of the file as HttpResponse
    '''
    filename = request.args.get('filename')
    if not filename:
        return HTTPResponse(status_code=400, reason='Bad Request')
    filepath = os.path.join(os.getcwd(), filename)
    if not os.path.isfile(filepath):
        return HTTPResponse(status_code=404, reason='File Not Found')
    with open(filepath, 'rb') as f:
        data = f.read()
    return HTTPResponse(
        status_code=200,
        headers={'Content-Type': 'application/octet-stream', 'Content-Disposition': f'attachment; filename="{filename}"'},
        body=data
    )