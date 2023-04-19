import hashlib

def certificate_matches(certificate: bytes, known_hash: str) -> bool:
    '''
    check if the certificate matches the known hash
    '''
    certificate_hash = hashlib.sha256(certificate).hexdigest()
    return certificate_hash == known_hash