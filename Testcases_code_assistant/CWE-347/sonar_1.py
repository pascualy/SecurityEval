import jwt

def verifyJWTToken(token):
    '''
    decode JWT Token and send the payload
    '''
    try:
        # decode the token using the secret key
        payload = jwt.decode(token, 'secret_key', algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        # token has expired
        return "Token has expired"
    except jwt.InvalidTokenError:
        # token is invalid
        return "Invalid token"