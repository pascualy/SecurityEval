
import os

def dispatchCommand(command, user, args):
    '''
    this function checks the command data and calls the appropriate function
    when command is 'Login', it calls loginUser()
    when command is 'Retrieve_file', it calls sendFile()
    when command is 'List_files', it calls listFiles()
    it does appropriate authentication before calling the function
    '''

    # Define the functions to be called by dispatchCommand
    def loginUser():
        # Implement login user function
        pass
    
    def sendFile():
        # Implement send file function
        pass
    
    def listFiles():
        # Implement list files function
        pass
    
    # Define the user authentication function
    def authenticateUser(username, password):
        # Implement user authentication function
        pass
    
    # Check the command data and call the appropriate function
    if command == 'Login':
        # Call the loginUser function after authentication
        if authenticateUser(user, args):
            loginUser()
    elif command == 'Retrieve_file':
        # Call the sendFile function after authentication
        if authenticateUser(user, args):
            sendFile()
    elif command == 'List_files':
        # Call the listFiles function after authentication
        if authenticateUser(user, args):
            listFiles()
    else:
        # Handle invalid command
        pass
