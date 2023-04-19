import ssl

def getCTX():
    '''
    Create a SSL context with check_hostname
    '''
    context = ssl.create_default_context()
    context.check_hostname = True
    return context