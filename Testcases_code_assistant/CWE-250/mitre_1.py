import os

def makeNewUserDir(username):
    '''
    create a directory at the /home/ directory for the given username
    before creating the directory increase the privilege using raisePrivileges()
    lower the privilege using lowerPrivileges() after creating the directory
    handle the exception if the directory already exists
    '''
    try:
        # increase the privilege
        os.system('sudo -s')
        
        # create the directory
        os.mkdir('/home/' + username)
        
        # lower the privilege
        os.system('exit')
        
    except FileExistsError:
        print("Directory already exists")