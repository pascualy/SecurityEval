import hashlib

def storePassword(userName, password):
    '''
    Hashes the password and updates the database with username and hashed password by updateUserLogin() method
    '''
    # Convert the password to bytes
    password = str.encode(password)
    
    # Hash the password using SHA-256 algorithm
    hashed_password = hashlib.sha256(password).hexdigest()
    
    # Call the updateUserLogin() method to update the database
    updateUserLogin(userName, hashed_password)