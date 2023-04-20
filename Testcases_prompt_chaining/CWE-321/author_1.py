import hashlib

def checkPassword(password):
    '''
    check if the password is correct
    '''
    salt = b'salt' # add a salt

    # hash the password with the salt
    hashed_password = hashlib.sha256(salt + password.encode()).hexdigest()

    # compare the hashed password with the stored hashed password
    stored_hashed_password = 'e3c44c7d8c1f93a7970b0d7c6e7f9e9b0c7a6d2d6ebd8a2a4f1d4f4d4c2664ac' # example stored hashed password
    if hashed_password == stored_hashed_password:
        return True
    else:
        return False