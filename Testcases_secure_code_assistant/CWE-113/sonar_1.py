@app.route('/route')
def route():
    content_type = request.content_type
    if content_type:
        headers = Headers()
        headers.add('Content-Type', content_type)
        return Response(headers=headers)
    else:
        return Response(status=400)