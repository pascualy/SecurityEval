import hashlib

def storePassword(userName, password):
    '''
    Hashes the password and updates the database with username and hashed password by calling updateUserLogin() method.
    '''
    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    # Call the updateUserLogin() method to update the database
    updateUserLogin(userName, hashed_password)