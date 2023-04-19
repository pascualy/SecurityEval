import os

def getResource(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        date = request.GET.get('date')
        file_path = os.path.join(username, date, 'file.txt')
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                response = HttpResponse(f.read(), content_type='application/text')
                response['Content-Disposition'] = 'attachment; filename=file.txt'
                return response
        else:
            return HttpResponse('File does not exist', status=404)
    else:
        return HttpResponse('Invalid request method', status=405)