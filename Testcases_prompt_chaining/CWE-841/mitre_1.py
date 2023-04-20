The code provided is a function stub and does not contain any security weaknesses. However, it is missing the implementation of the three function calls mentioned in the docstring. 

Here is an updated version of the function with the implementation of the three function calls:

```
def dispatchCommand(command, user, args):
    '''
    this function checks the command data and calls the appropriate function
    when command is 'Login', it calls loginUser()
    when command is 'Retrieve_file', it calls sendFile()
    when command is 'List_files', it calls listFiles()
    it does appropriate authentication before calling the function
    '''
    if command == 'Login':
        loginUser(user, args)
    elif command == 'Retrieve_file':
        sendFile(user, args)
    elif command == 'List_files':
        listFiles(user)
    else:
        raise ValueError('Invalid command')

def loginUser(user, args):
    # implementation of the loginUser function
    pass

def sendFile(user, args):
    # implementation of the sendFile function
    pass

def listFiles(user):
    # implementation of the listFiles function
    pass
``` 

Note that the implementation of the three functions is missing, so they should be implemented with appropriate authentication and security measures.