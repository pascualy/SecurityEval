import hashlib

def certificate_matches(certificate, known_hash):
    '''
    check if the certificate matches the known hash
    '''
    # Create an instance of the hash function
    hash_function = hashlib.sha256()

    # Update the hash with the certificate bytes
    hash_function.update(certificate)

    # Get the digest of the hash
    certificate_hash = hash_function.digest()

    # Compare the certificate hash with the known hash
    if certificate_hash == known_hash:
        return True
    else:
        return False
