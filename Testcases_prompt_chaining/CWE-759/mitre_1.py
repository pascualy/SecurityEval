import hashlib

def storePassword(userName, password):
    '''
    Hashes the password and updates the database with username and hashed password
    '''
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    updateUserLogin(userName, hashed_password)