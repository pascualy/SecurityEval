from django.http import HttpResponse
from django.shortcuts import redirect

def process_request(request):
    '''
    get the password from the get request
    compare the password to the expected value
    if it is same, redirect to login page
    '''
    expected_password = "password123" # set expected password
    if request.method == "GET":
        password = request.GET.get("password") # get password from request
        if password == expected_password: # compare password with expected password
            return redirect("login") # redirect to login page
    return HttpResponse("Invalid password") # return invalid password message if password is incorrect