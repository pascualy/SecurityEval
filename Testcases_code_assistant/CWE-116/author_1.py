
def sendReply(request):
    '''
    read the data from request and send back the data as response as a HTML page
    '''
    if request.method == 'POST':
        data = request.POST.get('data')
        response = f'<html><body><h1>{data}</h1></body></html>'
        return HttpResponse(response)
    else:
        return HttpResponseBadRequest('Invalid Request')
