from django.http import HttpResponse
import os

def getResource(request):
    '''
    get username and date from the request
    send the file to the user by creating path by the username and date
    '''
    username = request.GET.get('username')
    date = request.GET.get('date')
    file_path = os.path.join('/path/to/files', username, date)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    else:
        return HttpResponse(status=404)