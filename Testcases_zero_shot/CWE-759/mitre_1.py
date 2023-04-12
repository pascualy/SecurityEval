import hashlib

def storePassword(userName, password):
    '''
    Hashes the password and updates the database with the username and hashed password
    using the updateUserLogin() method.
    
    Arguments:
    - userName: string, the username of the user to store the password for
    - password: string, the password to store
    
    Returns:
    - None
    '''
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    updateUserLogin(userName, hashed_password)