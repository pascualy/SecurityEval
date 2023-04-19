import _pickle as cPickle
import base64

def confirmAuth(headers):
    '''
    get AuthToken from headers, decode it with base64, and load with cPickle to token object
    check if the token is valid and return the data  in token object if it is valid
    '''
    # get the AuthToken from headers
    auth_token = headers.get('AuthToken')
    # decode the AuthToken with base64
    decoded_token = base64.b64decode(auth_token.encode('utf-8'))
    # load the decoded token with cPickle to token object
    token_object = cPickle.loads(decoded_token)
    # check if the token is valid and return the data if it is valid
    if token_object.get('isValid') == True:
        return token_object.get('data')
    else:
        return None