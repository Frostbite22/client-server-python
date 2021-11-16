import socket
import subprocess
import os


pid = os.getpid()
with open("pid.txt","a+") as f:
    f.write(str(pid))
    f.write("\n")

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 9796    # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with open("log.txt",'a+') as log:
            log.write(str(addr))
            log.write("\n")
        with conn:
            while True:
                data = conn.recv(1024)
                print(data.decode())
                if not data:
                    break
                process = subprocess.Popen(['finger', data.decode()], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out, err = process.communicate()
                conn.sendall(out)
                conn.sendall("you are here".encode())

            
