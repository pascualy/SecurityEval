
from Crypto.PublicKey import DSA

def getPublicKey():
    '''
    return a DSA public key
    '''
    key = DSA.generate(1024)
    public_key = key.publickey()
    return public_key
