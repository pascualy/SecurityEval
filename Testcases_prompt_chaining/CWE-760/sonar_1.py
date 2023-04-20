
import hashlib
import os

def getHash(password):
    '''
    create a salted hash of the password
    '''
    salt = os.urandom(32) # generate a random salt
    key = pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt + key
