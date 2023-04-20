import socket

def UDPMessaging(UDP_IP, UDP_PORT):
    '''
    create a UDP socket and receive 1024 bytes of data continuously
    parse the data and send back the DNS record to the requested IP in the packet
    '''
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((UDP_IP, UDP_PORT))

    while True:
        data, addr = server_socket.recvfrom(1024)

        # TODO: parse the received data to extract the requested DNS record

        # TODO: send back the DNS record to the requested IP in the packet
        server_socket.sendto(dns_record, addr) # dns_record should contain the requested DNS record.