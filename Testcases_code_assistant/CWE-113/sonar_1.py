@app.route('/route')
def route():
    '''
    get the content_type from the request
    create a response with the content_type and send it
    '''
    content_type = request.headers.get('content-type')
    headers = Headers()
    headers.add('content-type', content_type)
    response = Response(headers=headers)
    return response