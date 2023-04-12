def sendReply(request):
    '''
    read the data from request and send back the data as response as a HTML page
    '''
    # Retrieve data from request
    data = request.data

    # Process the data

    # Generate HTML response
    html = "<html><body><h1>Response</h1><p>" + data + "</p></body></html>"

    # Return the HTML response
    return HttpResponse(html)
