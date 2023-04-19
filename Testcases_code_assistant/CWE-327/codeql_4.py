import hashlib

def get_password_hash(password: str, salt: str):
    '''
    return the hash of the password
    '''
    password = password.encode('utf-8') # convert password to bytes
    salt = salt.encode('utf-8') # convert salt to bytes
    hashed_password = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)
    return hashed_password.hex() # return hash as hexadecimal string