def getEncryptionKey(key):
    '''
    define a Cipher using AES and CBC mode
    encrypt the key using the cipher and return it
    '''

    # Generate a random 16 byte key
    iv = urandom(16)

    # Create the Cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))

    # Create the encryptor object
    encryptor = cipher.encryptor()

    # Encrypt the key
    encrypted_key = encryptor.update(key) + encryptor.finalize()

    return encrypted_key