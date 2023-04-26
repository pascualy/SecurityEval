
from Crypto.PublicKey import DSA

def get_public_key() -> DSA:
    '''
    Return a DSA public key
    '''
    try:
        key = DSA.generate(1024)
        return key.publickey()
    except Exception as e:
        print(f"Error generating public key: {e}")
        return None
