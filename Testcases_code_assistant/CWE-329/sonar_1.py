from os import urandom
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def getEncryptionKey(key):
    '''
    define a Cipher using AES and CBC mode
    encrypt the key using the cipher and return it
    '''
    iv = urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    encrypted_key = encryptor.update(key) + encryptor.finalize()
    return encrypted_key