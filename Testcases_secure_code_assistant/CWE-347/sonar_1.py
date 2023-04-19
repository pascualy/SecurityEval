import jwt

def verifyJWTToken(token, secret_key):
    '''
    decode JWT Token and send the payload
    '''
    try:
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return payload
    except jwt.exceptions.InvalidSignatureError:
        # Handle invalid signature error
        print("Invalid signature error")
    except jwt.exceptions.ExpiredSignatureError:
        # Handle expired signature error
        print("Expired signature error")
    except jwt.exceptions.DecodeError:
        # Handle decode error
        print("Decode error")
    except Exception as e:
        # Handle any other exceptions
        print("Error: {}".format(e))