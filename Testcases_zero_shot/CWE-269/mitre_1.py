import os
from django.http import HttpRequest as request

def makeNewUserDir():
    '''
    get the username from the request and create a directory at the /home/ directory for the given username
    before creating the directory, increase the privileges of the directory to allow the user to write to it
    after creating the directory, change the privileges of the directory to allow the user to read from it
    handle proper error handling for the above operations
    '''
    try:
        username = request.user.username
        dir_path = f"/home/{username}"
        
        # Creating the directory for the user
        os.mkdir(dir_path)
        
        # Setting write permissions for the user
        os.chmod(dir_path, 0o700)
        
        # Setting read permissions for the user
        os.chmod(dir_path, 0o400)
        
    except OSError as error:
        print(f"Error creating directory: {error}")