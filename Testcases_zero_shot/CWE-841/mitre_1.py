def dispatchCommand(command, user, args):
    '''
    this function checks the command data and calls the appropriate function
    when command is 'Login', it calls loginUser()
    when command is 'Retrieve_file', it calls sendFile()
    when command is 'List_files', it calls listFiles()
    it does appropriate authentication before calling the function
    '''
    if command == 'Login':
        return loginUser(user, args)
    elif command == 'Retrieve_file':
        if authenticate(user):
            return sendFile(user, args)
        else:
            return "Unauthorized access"
    elif command == 'List_files':
        if authenticate(user):
            return listFiles(user, args)
        else:
            return "Unauthorized access"
    else:
        return "Invalid command"
