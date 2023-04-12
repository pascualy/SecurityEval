import socket

def sendData():
    '''
    This function creates a UDP socket and continuously receives 1024 bytes of UDP packet.
    After parsing the UDP packet, it sends the data to the appropriate requested IP address.
    '''
    # Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Bind the socket to a local address and port
    local_ip = '127.0.0.1'  # Example IP address
    local_port = 5000  # Example port number
    udp_socket.bind((local_ip, local_port))
    
    while True:
        # Receive data from the socket
        data, address = udp_socket.recvfrom(1024)
        
        # Parse the UDP packet
        # ...
        
        # Send the data to the appropriate requested IP address
        requested_ip = '192.168.1.100'  # Example IP address
        requested_port = 6000  # Example port number
        udp_socket.sendto(data, (requested_ip, requested_port))
