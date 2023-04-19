import os

def makeNewUserDir(username):
    '''
    create a directory at the /home/ directory for the given username
    before creating the directory increase the privilege using raisePrivileges()
    lower the privilege using lowerPrivileges() after creating the directory
    handle the exception if the directory already exists
    '''
    # Function to raise privileges
    def raisePrivileges():
        if os.getuid() != 0:
            os.seteuid(0)
    
    # Function to lower privileges
    def lowerPrivileges():
        if os.getuid() == 0:
            os.seteuid(os.getlogin())

    # Raise privileges
    raisePrivileges()

    # Create directory
    try:
        os.mkdir('/home/{}'.format(username))
    except FileExistsError:
        print('Directory already exists')

    # Lower privileges
    lowerPrivileges()