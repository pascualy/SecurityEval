import hashlib

def checkPassword(password):
    '''
    Check if the password is correct
    
    Parameters:
    password (str): The password to be checked
    
    Returns:
    bool: True if the password is correct, False otherwise
    '''
    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    # Compare the hashed password with the correct hash
    correct_hash = '0c07a5378ddc5c5d5a2a9bce9e8ebd7b958c5e6f7e6f5a6d7c15d5f6a7c9a8b1'
    if hashed_password == correct_hash:
        return True
    else:
        return False