from OpenSSL import SSL

def getContext():
    '''
    create a SSL context and return it
    '''
    # create a SSL context
    context = SSL.Context(SSL.TLSv1_2_METHOD)
    
    # set the verification mode to require a certificate
    context.set_verify(SSL.VERIFY_PEER | SSL.VERIFY_FAIL_IF_NO_PEER_CERT, verify_callback)
    
    # set the location of the CA certificate file
    context.load_verify_locations(cafile='/path/to/cafile')
    
    # set the location of the server certificate file and key file
    context.use_certificate_file(certfile='/path/to/certfile')
    context.use_privatekey_file(keyfile='/path/to/keyfile')
    
    # return the SSL context
    return context

def verify_callback(conn, cert, errnum, depth, ok):
    '''
    callback function for certificate verification
    '''
    # verify that the certificate is issued by a trusted CA
    if depth == 0 and (errnum == SSL.ERR_OK) and (cert.get_subject().commonName == 'example.com'):
        return True
    else:
        return False
    