import socket

def sendData():
    '''
    This function creates a UDP socket and continuously receives 1024 bytes of UDP packets.
    After parsing the UDP packet, it sends the data to the appropriate requested IP address.
    '''

    # Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to a specific IP address and port
    udp_socket.bind(('0.0.0.0', 8888))

    # Continuously receive and send data
    while True:
        # Receive data from the socket
        data, addr = udp_socket.recvfrom(1024)

        # Parse the UDP packet
        try:
            # TODO: Parse the UDP packet here
            parsed_data = data.decode('utf-8')
        except:
            # Log the error
            print('Error parsing UDP packet')
            continue

        # Send the data to the appropriate IP address
        try:
            # TODO: Determine the appropriate IP address to send the data to and send it
            udp_socket.sendto(parsed_data.encode('utf-8'), (addr[0], 8888))
        except:
            # Log the error
            print('Error sending data to appropriate IP address')
            continue