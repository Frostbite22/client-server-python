import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 23        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    while True:
        data,adr = s.recvfrom(1024)
        print(data)
        # s.sendto(data.upper(),(HOST,PORT))
