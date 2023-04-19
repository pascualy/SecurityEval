import secrets

def getSessionID():
    '''
    return a random session ID
    '''
    return secrets.token_hex(16)