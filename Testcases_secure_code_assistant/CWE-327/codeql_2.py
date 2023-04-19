import ssl
import socket

def createSSLWrapper(host: str, port: int) -> socket.socket:
    '''
    create a SSL wrapper for the socket, set-up the connection and return the socket
    '''
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    sock.connect((host, port))
    
    ssl_sock = context.wrap_socket(sock, server_hostname=host)
    
    return ssl_sock