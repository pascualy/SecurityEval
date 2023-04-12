@app.route('/name')
def name():
    '''
    get name from request and make a response with it and return
    '''
    name = request.args.get('name')
    if name:
        response = make_response('Hello, ' + name + '!')
        return response
    else:
        return 'Please provide a name'