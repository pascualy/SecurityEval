import ssl
import socket

def createSSLWrapper(host, port):
    '''
    create a SSL wrapper for the socket, set-up the connection and return the socket
    '''
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    s.connect((host, port))

    # Create a SSL context
    context = ssl.create_default_context()

    # Wrap the socket with SSL
    ssl_socket = context.wrap_socket(s, server_hostname=host)

    # Return the SSL socket
    return ssl_socket