
import ssl
import socket

def createSSLWrapper(host, port):
    '''
    create a SSL wrapper for the socket, set-up the connection and return the socket
    '''
    context = ssl.create_default_context()
    sock = socket.create_connection((host, port))
    return context.wrap_socket(sock, server_hostname=host)
