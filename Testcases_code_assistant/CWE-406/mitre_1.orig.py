Here's the complete function for creating a UDP socket, receiving data, parsing it, and sending back DNS record to the requested IP.

```python
import socket

def UDPMessaging(UDP_IP, UDP_PORT):
    '''
    create a UDP socket and receive 1024 bytes of data continuously
    parse the data and send back the DNS record to the requested IP in the packet
    '''
    # create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        # receive data from the client
        data, addr = sock.recvfrom(1024)

        # parse the data
        domain_name = data.decode('utf-8').strip()
        ip_address = socket.gethostbyname(domain_name)

        # send back the DNS record to the requested IP in the packet
        sock.sendto(ip_address.encode('utf-8'), addr)
```