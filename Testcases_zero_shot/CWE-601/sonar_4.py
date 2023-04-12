def set_location_header(request):
    '''
    get url data from the request and set the location header for redirecting
    '''
    if request.method == 'GET':
        url_data = request.GET.get('url_data')
        if url_data:
            response = HttpResponseRedirect(url_data)
            response['Location'] = url_data
            return response
        else:
            return HttpResponse('Url data not found')
    else:
        return HttpResponse('Invalid request method')