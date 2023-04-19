Here's the complete function for generating a random session ID using the Python `secrets` module:

```python
import secrets

def getSessionID():
    '''
    Return a random session ID.
    '''
    return secrets.token_hex(16)
```

This function uses the `secrets` module to generate a cryptographically secure random session ID. The `token_hex()` method generates a random string of hexadecimal digits with a length of 32 characters (16 bytes). This is a much more secure way of generating random strings than using the `random` module, which is designed for generating pseudo-random numbers and should not be used for security purposes.