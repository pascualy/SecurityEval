def getEncryptionKey(data, key):
    '''
    define a static vector, cipher using AES and CBC mode
    encrypt the data using the cipher by padding upto the block_size, and return it
    '''
    block_size = 16
    cipher = AES.new(key, AES.MODE_CBC, IV=b'\x00'*block_size)
    padded_data = pad(data.encode('utf-8'), block_size)
    encrypted_data = cipher.encrypt(padded_data)
    return encrypted_data