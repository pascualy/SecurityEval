from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

def getEncryptionKey(data, key):
    '''
    generate a random 16-byte IV
    define cipher using AES and CBC mode
    encrypt the data using the cipher by padding up to the block_size, and return it
    '''
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(data.encode(), AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    return encrypted_data