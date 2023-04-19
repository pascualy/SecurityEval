import ssl

def getCTX():
    '''
    Create a SSL stdlib context
    '''
    context = ssl.create_default_context()
    context.check_hostname = True
    context.verify_mode = ssl.CERT_REQUIRED
    return context