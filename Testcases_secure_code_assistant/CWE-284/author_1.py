
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def getContent(request):
    '''
    Check if the request is a GET request
    If it is, make ACCESS_DENIED False
    If the user is not authenticated, ACCESS_DENIED will already be True due to the @login_required decorator
    If ACCESS_DENIED is True, redirect to the login page, otherwise return to the content page
    '''
    if request.method == 'GET':
        ACCESS_DENIED = False
    else:
        ACCESS_DENIED = True

    if ACCESS_DENIED:
        return redirect('login')
    else:
        return render(request, 'content.html')
