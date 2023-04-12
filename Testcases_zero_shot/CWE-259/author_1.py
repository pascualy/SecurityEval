def checkAdminPassword(password):
    '''
    Check if the password is valid for admin.
    Returns True if it is, False otherwise.
    '''
    ADMIN_PASSWORD = "admin123" # Replace with the actual admin password
    
    if password == ADMIN_PASSWORD:
        return True
    else:
        return False
