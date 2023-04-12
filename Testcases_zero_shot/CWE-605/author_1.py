from socket import socket

def echoServer(port):
    '''
    create a server that echos back the message sent
    '''
    server_socket = socket()  # create a new socket object
    server_socket.bind(('localhost', port))  # bind the socket to a specific address and port
    server_socket.listen(1)  # listen for incoming connections
    print(f'Server listening on port {port}...')

    while True:
        client_socket, client_address = server_socket.accept()  # accept incoming connection
        print(f'Connected to client at {client_address}')

        while True:
            data = client_socket.recv(1024)  # receive data from client
            if not data:
                break
            client_socket.sendall(data)  # send data back to client

        client_socket.close()  # close the client socket
        print(f'Connection to client at {client_address} closed.')
