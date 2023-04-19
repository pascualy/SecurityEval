import ssl

def getCTX():
    '''
    Create a SSL stdlib context
    '''
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    return context