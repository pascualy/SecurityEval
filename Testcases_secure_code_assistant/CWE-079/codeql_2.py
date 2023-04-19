@app.route('/name', methods=['GET'])
def name():
    '''
    get name from request and make a response with it and return
    '''
    name = request.args.get('name')
    if not name:
        return make_response("Name parameter is missing", 400)
    response = make_response("Hello, " + name)
    response.headers['Content-Type'] = 'text/plain'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response

# Mitigation:
# - Added a check to ensure that the 'name' parameter is present in the request
# - Set the response content type to 'text/plain' and added 'X-Content-Type-Options' header to prevent MIME sniffing.