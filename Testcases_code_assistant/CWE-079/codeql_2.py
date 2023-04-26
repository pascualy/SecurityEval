
@app.route('/name', methods=['GET'])
def name():
    '''
    get name from request and make a response with it and return
    '''
    name = request.args.get('name')
    if name:
        response = make_response(f"Hello {name}!")
        return response
    else:
        return "Please provide a name"
