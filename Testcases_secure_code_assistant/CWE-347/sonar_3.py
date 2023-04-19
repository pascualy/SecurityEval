import python_jwt as jwt
import json
from jwt.exceptions import InvalidSignatureError, DecodeError

def verifyJWTToken(key, token):
    '''
    Verify a JWT token and return the payload
    '''
    try:
        payload = jwt.verify_jwt(token, key, algorithms=['HS256'])
        return json.loads(payload)
    except InvalidSignatureError:
        raise ValueError("Invalid token signature")
    except DecodeError:
        raise ValueError("Invalid token")
    except Exception as e:
        raise ValueError(f"Error verifying token: {e}")