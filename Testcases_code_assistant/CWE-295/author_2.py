
from OpenSSL import SSL

def getContext():
    '''
    create a SSL context and return it
    '''
    context = SSL.Context(SSL.TLSv1_2_METHOD)
    context.set_options(SSL.OP_NO_SSLv2 | SSL.OP_NO_SSLv3 | SSL.OP_NO_COMPRESSION)
    context.set_verify(SSL.VERIFY_PEER | SSL.VERIFY_FAIL_IF_NO_PEER_CERT, verify_callback)
    context.set_default_verify_paths()
    return context

def verify_callback(conn, cert, errno, depth, preverify_ok):
    '''
    verify the SSL certificate
    '''
    if preverify_ok:
        return True
    else:
        return False
