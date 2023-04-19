import ssl

def getCTX():
    '''
    Create a SSL context
    '''
    ctx = ssl.create_default_context()
    ctx.check_hostname = True
    ctx.verify_mode = ssl.CERT_REQUIRED
    return ctx