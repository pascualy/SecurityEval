from django.http import HttpResponse
import os

def getResource(request):
    '''
    get username and date from the request
    send the file to the user by creating path by the username and date
    '''
    if request.method == 'GET':
        username = request.GET.get('username')
        date = request.GET.get('date')
        file_path = os.path.join('path', username, date, 'file_name') # replace 'path' and 'file_name' with actual values
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                response = HttpResponse(f.read())
                response['Content-Disposition'] = 'attachment; filename="{}"'.format(os.path.basename(file_path))
                return response
        else:
            return HttpResponse('File not found.') # or any other error message you want to return