import hashlib

def checkPassword(password):
    '''
    Check if the password is correct
    '''

    # Convert the password to bytes and hash it using SHA256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Compare the hashed password with a pre-defined hash value
    if hashed_password == 'f1c9645dbc14efddc7d8a322685f26eb4b834290beac24b82a2c21fdb0d4f9e6':
        print("Password is correct")
    else:
        print("Password is incorrect")