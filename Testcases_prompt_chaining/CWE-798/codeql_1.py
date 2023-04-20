from django.http import HttpResponse
from django.shortcuts import redirect

def process_request(request):
    '''
    get the password from the POST request
    compare the password to the expected value
    if it is same, redirect to login page
    '''
    if request.method == 'POST':
        password = request.POST.get('password')
        expected_password = 'password123' # replace with actual expected password
        if password == expected_password:
            return redirect('login')
    return HttpResponse('Invalid password') # return an error message if the password is incorrect