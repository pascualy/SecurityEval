import secrets

def generateRandomString(length):
    '''
    Generates a cryptographically secure random string of fixed length.
    '''
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(length))