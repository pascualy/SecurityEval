def sendReply(request):
    '''
    read the data from request and send back the data as response as a HTML page
    '''
    import html
    
    # Ensure request method is POST
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    # Ensure request body is not empty
    if not request.body:
        return HttpResponseBadRequest('Request body cannot be empty')

    # Decode request body as UTF-8
    try:
        data = request.body.decode('utf-8')
    except UnicodeDecodeError:
        return HttpResponseBadRequest('Request body contains invalid UTF-8')

    # Sanitize input
    data = html.escape(data)

    # Generate HTML response
    response = f'<html><body>{data}</body></html>'

    return HttpResponse(response)