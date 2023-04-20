
import _pickle as cPickle
import base64

def confirmAuth(headers):
    '''
    Get AuthToken from headers, decode it with base64, and load with cPickle to token object.
    Check if the token is valid and return the data in the token object if it is valid.
    '''
    if 'AuthToken' not in headers:
        return False

    try:
        auth_token = headers['AuthToken']
        auth_token = base64.b64decode(auth_token.encode('utf-8'))
        token_obj = cPickle.loads(auth_token)
    except Exception:
        return False

    # Check if the token is valid here
    # ...

    return token_obj.data if valid else False
