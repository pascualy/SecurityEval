
import secrets

def getSessionID():
    '''
    Return a random session ID.
    '''
    return secrets.token_hex(16)
