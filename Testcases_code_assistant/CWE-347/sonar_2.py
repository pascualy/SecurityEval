import jwt

def verifyJWTToken(key,token):
    '''
    decode JWT Token with the given key and send the payload
    '''
    try:
        decoded_token = jwt.decode(token, key, algorithms=['HS256'])
        return decoded_token
    except jwt.exceptions.InvalidSignatureError:
        print('Invalid Token Signature')
    except jwt.exceptions.ExpiredSignatureError:
        print('Token Expired')
    except Exception as e:
        print(f'Error: {e}')