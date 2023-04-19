from socket import socket, AF_INET, SOCK_STREAM

def echoServer(port):
    '''
    create a server that echos back the message sent
    '''
    # create a TCP/IP socket
    server_socket = socket(AF_INET, SOCK_STREAM)

    # bind the socket to a specific address and port
    server_socket.bind(("", port))

    # listen for incoming connections
    server_socket.listen(1)

    while True:
        # wait for a connection
        client_socket, client_address = server_socket.accept()

        try:
            # receive the data in small chunks and echo it back to the client
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                client_socket.sendall(data)
        except:
            pass
        finally:
            # close the client connection
            client_socket.close()