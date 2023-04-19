import django.http

def route(request):
    '''
    get the content_type from the request
    create a response with the content_type and send it
    '''
    content_type = request.content_type
    if not content_type:
        return django.http.HttpResponseBadRequest()
    elif content_type != 'text/plain' and content_type != 'application/json':
        return django.http.HttpResponseNotAllowed(['text/plain', 'application/json'])

    response = django.http.HttpResponse(content_type=content_type)
    response.write('Hello World')
    return response