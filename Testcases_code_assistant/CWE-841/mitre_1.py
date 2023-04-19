def dispatchCommand(command, user, args):
    def authenticate():
        # function to authenticate user
        pass
    
    def loginUser():
        # function to handle login command
        pass
    
    def sendFile():
        # function to handle retrieve_file command
        pass
    
    def listFiles():
        # function to handle list_files command
        pass
    
    if command == 'Login':
        authenticate()
        loginUser()
    elif command == 'Retrieve_file':
        authenticate()
        sendFile()
    elif command == 'List_files':
        authenticate()
        listFiles()
    else:
        print("Invalid command")