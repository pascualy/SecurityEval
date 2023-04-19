import socket

def sendData():
    '''
    this function create UDP socket and continuesly recive 1024 bytes of UDP packet
    after parsing UDP packet, it sends the data to appropriate requested IP address
    '''
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to a specific address and port
    server_address = ('localhost', 10000)
    sock.bind(server_address)

    while True:
        # Receive data in chunks of 1024 bytes
        data, address = sock.recvfrom(1024)

        # Parse the UDP packet
        # Do some processing on the data

        # Send the processed data to the appropriate address
        # Note: This is just an example and will not work as is
        # You will need to modify it to fit your specific use case
        client_address = ('localhost', 20000)
        sock.sendto(processed_data, client_address)