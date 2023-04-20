from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def getContent(request):
    '''
    check if the request is a get request
    if it is, return to the content page
    '''
    if request.method == 'GET':
        return render(request, 'content.html')