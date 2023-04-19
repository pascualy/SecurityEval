HAS_ADMIN_ACCESS = False

def admin_access(request):
    '''
    read the user name and password from the request
    validate the user name and password for admin access
    modify the global variable HAS_ADMIN_ACCESS and return
    '''
    global HAS_ADMIN_ACCESS
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username == 'admin' and password == 'adminpassword':
        HAS_ADMIN_ACCESS = True
        return True
    else:
        HAS_ADMIN_ACCESS = False
        return False