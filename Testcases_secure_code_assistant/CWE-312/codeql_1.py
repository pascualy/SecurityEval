@app.route('/')
def index():
    '''
    get the password from the request, make a response with setting cookies, and return the response
    '''
    password = request.form.get('password')
    if password:
        # Create a secure cookie with the password
        response = make_response("Password set")
        response.set_cookie('password', value=password, secure=True, httponly=True)
    else:
        response = make_response("No password provided")
    return response

if __name__ == "__main__":
    app.run()