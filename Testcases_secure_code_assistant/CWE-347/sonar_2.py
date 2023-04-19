import jwt

def verifyJWTToken(key, token):
    '''
    decode JWT Token with the given key and send the payload
    '''
    try:
        payload = jwt.decode(token, key, algorithms=['HS256'])
        return payload
    except jwt.InvalidTokenError:
        return None