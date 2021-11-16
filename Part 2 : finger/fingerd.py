import socket
import subprocess

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 9797    # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            print(data.decode())
            if not data:
                break
            process = subprocess.Popen(['finger', data.decode()], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = process.communicate()
            conn.sendall(out)

            
