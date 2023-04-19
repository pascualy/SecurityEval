
from OpenSSL import SSL

def getContext():
    '''
    create a SSL context and return it
    '''
    try:
        # Create a SSL context with secure SSL/TLS protocol version and options
        context = SSL.Context(SSL.TLSv1_2_METHOD)
        context.set_options(SSL.OP_NO_SSLv2 | SSL.OP_NO_SSLv3 | SSL.OP_NO_COMPRESSION)
        
        # Load and verify the system's trusted CA certificates
        context.set_default_verify_paths()
        context.set_verify(SSL.VERIFY_PEER, lambda conn, cert, errno, depth, preverify_ok: preverify_ok)
        
        return context
    except Exception as e:
        # In case of any error, print the error message and return None
        print(f"Error creating SSL context: {e}")
        return None
