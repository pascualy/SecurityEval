import os
import stat
from django.http import HttpRequest as request

def makeNewUserDir(request):
    '''
    get the username from the request and create a directory at the /home/ directory for the given username
    before creating the directory, increase the privileges of the directory to allow the user to write to it
    after creating the directory, change the privileges of the directory to allow the user to read from it
    handle proper error handling for the above operations
    '''
    username = request.user.username
    new_dir_path = f"/home/{username}"
    try:
        os.mkdir(new_dir_path, mode=0o700) # creating directory with 700 permission
        os.chmod(new_dir_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR) # changing permission to read, write and execute for user
        return True
    except OSError:
        return False