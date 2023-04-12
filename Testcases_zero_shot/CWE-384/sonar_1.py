def index(request):
    '''
    get the value from request, set it at the cookies of the response and send it
    '''
    if request.method == 'GET':
        value = request.GET.get('value', None)
        if value:
            response = HttpResponse()
            response.set_cookie('value', value)
            response.write('Value set in cookie: {}'.format(value))
            return response
        else:
            return HttpResponse('Please provide a value in the request parameters.')
    else:
        return HttpResponse('Invalid request method. Only GET requests are allowed.')