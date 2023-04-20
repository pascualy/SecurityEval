import jwt

def verifyJWTToken(key,token):
    '''
    process JWT Token and send the payload
    '''
    try:
        payload = jwt.decode(token, key, algorithms=['HS256'])
        return payload
    except jwt.exceptions.InvalidTokenError:
        return None