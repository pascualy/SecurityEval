import jwt

def verifyJWTToken(key,token):
    '''
    decode JWT Token with the given key and send the payload
    '''
    try:
        decoded_payload = jwt.decode(token, key, algorithms=['HS256'])
        return decoded_payload
    except jwt.exceptions.InvalidSignatureError:
        return "Invalid Token Signature"
    except jwt.exceptions.DecodeError:
        return "Invalid Token"