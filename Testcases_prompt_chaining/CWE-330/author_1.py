import secrets

def getSessionID():
    '''
    return a cryptographically secure random session ID
    '''
    return secrets.token_hex(16)