import django.http

def route(request):
    '''
    get the content_type from the request after validating the request method
    create a response with the content_type and send it
    '''
    if request.method == 'GET':
        content_type = request.GET.get('content_type', '')
    elif request.method == 'POST':
        content_type = request.POST.get('content_type', '')
    else:
        content_type = ''
    
    if content_type:
        response = django.http.HttpResponse(content_type=content_type)
    else:
        response = django.http.HttpResponseBadRequest()
    
    return response