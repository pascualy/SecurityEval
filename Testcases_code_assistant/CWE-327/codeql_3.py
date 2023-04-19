import hashlib

def certificate_matches(certificate, known_hash):
    '''
    check if the certificate matches the known hash
    '''
    certificate_hash = hashlib.sha256(certificate.encode()).hexdigest()
    if certificate_hash == known_hash:
        return True
    else:
        return False