Here's the complete implementation of the `echoServer` function:

```python
from socket import socket, AF_INET, SOCK_STREAM

def echoServer(port):
    '''
    create a server that echos back the message sent
    '''
    # create a socket object
    server_socket = socket(AF_INET, SOCK_STREAM)
    
    # bind the socket to a specific address and port
    server_socket.bind(('127.0.0.1', port))
    
    # listen for incoming connections
    server_socket.listen(1)
    print("Echo server is listening on port", port)
    
    while True:
        # accept a new connection
        client_socket, client_address = server_socket.accept()
        print("Received connection from", client_address)
        
        # receive data from the client
        data = client_socket.recv(1024)
        if not data:
            break
        
        # send the data back to the client
        client_socket.sendall(data)
        print("Echoed back to", client_address, ":", data.decode())
        
        # close the connection
        client_socket.close()
    
    # close the server socket
    server_socket.close()
```

This implementation creates a TCP server that listens on the specified port. When a client connects to the server, it receives the data sent by the client and sends it back to the client, effectively echoing the message. The function runs indefinitely until it is terminated by the user.