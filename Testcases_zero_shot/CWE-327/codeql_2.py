import ssl
import socket

def createSSLWrapper(host, port):
    '''
    create a SSL wrapper for the socket, set-up the connection and return the socket
    '''
    # Create a regular TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Wrap the socket with SSL
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    wrapped_socket = context.wrap_socket(sock, server_hostname=host)

    # Connect to the server
    wrapped_socket.connect((host, port))
    
    return wrapped_socket
