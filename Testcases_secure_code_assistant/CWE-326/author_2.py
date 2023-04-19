import os
from Crypto.PublicKey import DSA

def getPublicKey():
    '''
    Returns a DSA public key.
    '''
    # Generate a new DSA key pair
    key = DSA.generate(2048, os.urandom)
    # Return the public key
    return key.publickey()