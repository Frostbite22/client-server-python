import socket
import sys
import getopt

argv = sys.argv[1:]
opts, args = getopt.getopt(argv,'l:h',['login=','host='])

for opt, arg in opts:
    if opt in ('-l','--login'):
        LOGIN = arg
    elif opt in ('-h'',--host'):
        HOST = arg



HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 9796  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(LOGIN.encode())
    data = s.recv(1024)
    data2 = s.recv(1024)

print(data.decode())
print(data2.decode())