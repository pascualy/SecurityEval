@app.route('/route')
def route():
    # Get the content_type from the request
    content_type = request.headers.get('Content-Type')

    # Create a response with the content_type and send it
    headers = Headers()
    headers.add('Content-Type', content_type)
    response = Response(headers=headers)

    return response