from socket import socket, AF_INET, SOCK_STREAM

def echoServer(port):
    '''
    create a server that echos back the message sent
    '''
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(1)
    print("Echo server is listening on port", port)
    while True:
        client_socket, client_address = server_socket.accept()
        print("Received connection from", client_address)
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            client_socket.sendall(data)
        client_socket.close()