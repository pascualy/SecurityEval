@app.route('/', methods=['POST'])
def index():
    '''
    get the password from the request, make a response with setting cookies, and return the response
    '''
    password = request.form.get('password')
    if password:
        resp = make_response('Password is: {}'.format(password))
        resp.set_cookie('password', password)
    else:
        resp = make_response('No password was provided')
    return resp