def getHash(password):
    '''
    create a hash of the password with the salt
    '''
    salt = b'salt'
    iterations = 100000
    key_length = 32
    hash_algorithm = 'sha256'
    byte_password = password.encode('utf-8')
    
    hashed_password = pbkdf2_hmac(hash_algorithm, byte_password, salt, iterations, key_length)
    
    return hashed_password.hex()