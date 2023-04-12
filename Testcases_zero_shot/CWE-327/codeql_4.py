import hashlib

def get_password_hash(password: str, salt: str):
    '''
    return the hash of the password
    '''
    password_salt = password + salt
    password_hash = hashlib.sha256(password_salt.encode('utf-8')).hexdigest()
    return password_hash