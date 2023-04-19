def getContent(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            ACCESS_DENIED = False
        else:
            ACCESS_DENIED = True

        if ACCESS_DENIED:
            return redirect('login')
        else:
            return render(request, 'content.html')