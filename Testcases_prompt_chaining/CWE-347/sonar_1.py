import jwt

def verifyJWTToken(token, secret_key):
    '''
    decode JWT Token and send the payload
    '''
    try:
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return payload
    except jwt.exceptions.InvalidTokenError:
        return False