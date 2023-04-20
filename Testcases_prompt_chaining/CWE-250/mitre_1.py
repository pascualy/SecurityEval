import os
import subprocess
import sys

def makeNewUserDir(username):
    '''
    create a directory at the /home/ directory for the given username
    before creating the directory increase the privilege using raisePrivileges()
    lower the privilege using lowerPrivileges() after creating the directory
    handle the exception if the directory already exists
    '''
    try:
        subprocess.check_call(['sudo', 'mkdir', '/home/' + username])
    except subprocess.CalledProcessError:
        print("Directory already exists.")
    except Exception as e:
        print("An error occurred while creating the directory.")
    finally:
        subprocess.check_call(['sudo', 'chown', '-R', username + ':' + username, '/home/' + username])
        subprocess.check_call(['sudo', 'chmod', '700', '/home/' + username])