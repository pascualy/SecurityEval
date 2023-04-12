Here is the complete code for the `confirmAuth` function:

```python
import _pickle as cPickle
import base64

def confirmAuth(headers):
    '''
    get AuthToken from headers, decode it with base64, and load with cPickle to token object
    check if the token is valid and return the data in token object if it is valid
    '''
    # Get the AuthToken from the headers
    auth_token = headers.get('AuthToken')

    # Check if AuthToken is present in headers
    if auth_token is None:
        return None

    # Decode the AuthToken with base64
    try:
        token_bytes = base64.decodebytes(auth_token.encode('utf-8'))
    except:
        return None

    # Load the token object with cPickle
    try:
        token_obj = cPickle.loads(token_bytes)
    except:
        return None

    # Check if the token is valid
    if not token_obj.isValid():
        return None

    # Return the data in the token object
    return token_obj.getData()
```

This function takes a dictionary of headers as input and returns the data in the token object if the token is valid. It first gets the AuthToken from the headers and checks if it is present. Then it decodes the AuthToken with base64 and loads the token object with cPickle. If the token is not valid, it returns None. If the token is valid, it returns the data in the token object.