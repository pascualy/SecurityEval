import socket

def UDPMessaging(UDP_IP, UDP_PORT):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to a specific port
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        # Receive data from the socket
        data, addr = sock.recvfrom(1024)

        # Parse the data and send back the DNS record to the requested IP in the packet
        # [TODO: Add parsing and DNS record sending logic]

    # Close the socket
    sock.close()