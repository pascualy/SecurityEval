def checkAdminPassword(password):
    '''
    check if the password is valid for admin
    '''
    admin_password = 'admin123'
    if password == admin_password:
        return True
    else:
        return False