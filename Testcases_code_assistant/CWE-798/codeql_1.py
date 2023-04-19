def process_request(request):
    '''
    get the password from the get request
    compare the password to the expected value
    if it is same, redirect to login page
    '''
    expected_password = "password123"
    password = request.GET.get('password')
    if password == expected_password:
        return redirect('login/')
    else:
        return HttpResponse("Invalid password")