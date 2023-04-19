import python_jwt as jwt
def verifyJWTToken(key,token):
    '''
    process JWT Token and send the payload
    '''
    try:
        payload, header = jwt.verify_jwt(token, key, algorithms=['HS256'])
        return payload
    except jwt.InvalidTokenError:
        return None