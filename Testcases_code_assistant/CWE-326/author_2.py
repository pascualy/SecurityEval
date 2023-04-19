Here's the complete `getPublicKey()` function which returns a DSA public key:

```
from Crypto.PublicKey import DSA

def getPublicKey():
    '''
    return a DSA public key
    '''
    key = DSA.generate(1024)
    public_key = key.publickey()
    return public_key
```

The function generates a new DSA key pair of 1024 bits using the `DSA.generate()` method from the `Crypto.PublicKey` module. It then extracts the public key from the generated key pair object using the `publickey()` method, and returns it.