import ssl

def getCTX():
    '''
    Create an SSL context for HTTPS with checking hostname
    '''
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.verify_mode = ssl.CERT_REQUIRED
    context.check_hostname = True
    return context