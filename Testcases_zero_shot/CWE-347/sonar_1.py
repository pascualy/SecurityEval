import jwt

def verifyJWTToken(token):
    '''
    decode JWT Token and send the payload
    '''
    try:
        decoded_token = jwt.decode(token, verify=False)
        return decoded_token
    except jwt.exceptions.DecodeError:
        print("Invalid Token")
    except jwt.exceptions.InvalidTokenError:
        print("Invalid Token")