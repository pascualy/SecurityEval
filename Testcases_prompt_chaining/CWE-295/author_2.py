from OpenSSL import SSL

def getContext():
    '''
    create a SSL context and return it
    '''
    # Load trusted CA certificates
    ca_cert = "/path/to/ca/cert"
    context = SSL.Context(SSL.TLSv1_2_METHOD)
    context.load_verify_locations(ca_cert)

    # Load client certificate and private key
    client_cert = "/path/to/client/cert"
    private_key = "/path/to/private/key"
    context.use_certificate_file(client_cert)
    context.use_privatekey_file(private_key)

    return context