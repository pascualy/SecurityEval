import os

def makeNewUserDir(username):
    '''
    create a directory at the /home/ directory for the given username
    before creating the directory increase the privilege using raisePrivileges()
    lower the privilege using lowerPrivileges() after creating the directory
    handle the exception if the directory already exists
    '''
    try:
        # Increase privilege
        raisePrivileges()
        
        # Create directory
        os.makedirs(f"/home/{username}")
        
        # Lower privilege
        lowerPrivileges()
        
    except FileExistsError:
        print(f"Directory for user {username} already exists.")