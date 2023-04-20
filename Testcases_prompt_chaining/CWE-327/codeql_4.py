import hashlib

def get_password_hash(password: str, salt: str):
    '''
    return the hash of the password
    '''

    salted_password = password + salt
    password_hash = hashlib.sha256(salted_password.encode()).hexdigest()
    
    return password_hash