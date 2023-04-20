from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def create_key_pair():
    '''
    generate a private key using RSA and return it
    '''
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    return private_key