import hashlib

def checkPassword(password):
    '''
    check if the password is correct
    '''
    hash_object = hashlib.sha256(password.encode())
    hashed_password = hash_object.hexdigest()
    # add your password hash here
    correct_password_hash = "c9f0f895fb98ab9159f51fd0297e236d"
    
    if hashed_password == correct_password_hash:
        return True
    else:
        return False