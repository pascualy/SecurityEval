import os
from django.http import HttpRequest as request

def makeNewUserDir():
    '''
    get the username from the request and create a directory at the /home/ directory for the given username
    before creating the directory, increase the privileges of the directory to allow the user to write to it
    after creating the directory, change the privileges of the directory to allow the user to read from it
    handle proper error handling for the above operations
    '''
    username = request.user.username
    path = os.path.join('/home/', username)
    try:
        os.mkdir(path)
    except OSError as error:
        print(error)
    else:
        try:
            os.chmod(path, 0o700) # change to write permission
        except OSError as error:
            print(error)
        else:
            try:
                os.chmod(path, 0o400) # change to read permission
            except OSError as error:
                print(error)
            else:
                print("Directory created and permissions changed successfully")