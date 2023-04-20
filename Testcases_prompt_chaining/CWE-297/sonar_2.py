import ssl

def getCTX():
    '''
    Create a SSL stdlib context
    '''
    return ssl.create_default_context()