import secrets

def getRandomBits():
    '''
    get random 128 bits using secrets module
    '''
    return secrets.token_bytes(16)