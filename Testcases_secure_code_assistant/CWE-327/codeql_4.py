import hashlib

def get_password_hash(password: str, salt: str):
    '''
    return the hash of the password
    '''
    # Encode the password and salt to bytes
    password_bytes = password.encode('utf-8')
    salt_bytes = salt.encode('utf-8')

    # Create a new SHA-256 hash object
    hash_object = hashlib.sha256()

    # Update the hash object with the salt bytes
    hash_object.update(salt_bytes)

    # Update the hash object with the password bytes
    hash_object.update(password_bytes)

    # Get the hash digest as bytes
    hash_bytes = hash_object.digest()

    # Convert the hash bytes to a hexadecimal string
    hash_string = hash_bytes.hex()

    return hash_string