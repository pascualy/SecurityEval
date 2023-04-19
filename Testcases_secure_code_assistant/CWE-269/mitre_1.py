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
        new_dir = "/home/" + username
        os.mkdir(new_dir)
        os.chmod(new_dir, 0o700)
        os.chmod(new_dir, 0o500)
    except OSError:
        print("Creation of the directory failed")
    except Exception as e:
        print("An error occurred: ", e)