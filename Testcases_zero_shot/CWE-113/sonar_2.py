def route(request):
    '''
    get the content_type from the request
    create a response with the content_type and send it
    '''
    content_type = request.content_type
    response = django.http.HttpResponse(content_type=content_type)
    return response