import _pickle as cPickle
import base64

def confirmAuth(headers):
    '''
    get AuthToken from headers, decode it with base64, and load with cPickle to token object
    check if the token is valid and return the data in token object if it is valid
    '''
    if 'AuthToken' not in headers:
        return None
    
    auth_token = headers['AuthToken']
    
    try:
        token_data = cPickle.loads(base64.b64decode(auth_token))
    except:
        return None
    
    if 'username' not in token_data or 'expiration' not in token_data or 'signature' not in token_data:
        return None
    
    # check if the token has expired
    if token_data['expiration'] < time.time():
        return None
    
    # check the signature of the token
    signature = hmac.new(SECRET_KEY, msg=auth_token.encode(), digestmod=hashlib.sha256).hexdigest()
    if signature != token_data['signature']:
        return None
    
    # return the data in token object
    return token_data['username']