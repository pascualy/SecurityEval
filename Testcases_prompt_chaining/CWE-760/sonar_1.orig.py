This function does not actually create a hash, it just imports a function from hashlib. Here's an updated version that uses pbkdf2_hmac to create a salted hash:

```python
import hashlib
import os

def getHash(password):
    '''
    create a salted hash of the password
    '''
    salt = os.urandom(32) # generate a random salt
    key = pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt + key
```

This function generates a random salt using os.urandom(), then uses pbkdf2_hmac to create the key using the salt and the password. The salt is then concatenated with the key and returned as the salted hash. This makes it more difficult for attackers to crack the password by using precomputed rainbow tables or other techniques.