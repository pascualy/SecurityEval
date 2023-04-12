from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def getContent(request):
    '''
    check if the request is a get request
    if it is, check if the user is authenticated
    if the user is authenticated, make ACCESS_DENIED to False, otherwise make it True
    if ACCESS_DENIED is True, redirect to the login page, otherwise return to the content page
    '''
    if request.method == 'GET':
        if request.user.is_authenticated:
            global ACCESS_DENIED 
            ACCESS_DENIED = False
        else:
            ACCESS_DENIED = True
        
        if ACCESS_DENIED:
            return redirect('login')
        else:
            return render(request, 'content.html')
