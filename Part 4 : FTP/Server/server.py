import socket
import sys
import time
import os
import struct

print("\nWelcome to the FTP server.\n\nTo get started, connect a client.")

# Initialise socket stuff
TCP_IP = "127.0.0.1" # Only a local server
TCP_PORT = 1423 # Just a random choice
BUFFER_SIZE = 1024 # Standard size
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()

print("\nConnected to by address: {}".format(addr))

def upld():
    return

def list_files():
    return

def dwld():
    while True :
        data = conn.recv(1024)
        f = open(data,'rb')
        l = f.read(1024)
        while (l):
            conn.send(l)
            print('Sent ',repr(l))
            l = f.read(1024)
        f.close()

    return


def delf():
   return 
       


def quit():
    # Send quit conformation
    conn.send("1")
    # Close and restart the server
    conn.close()
    s.close()
    os.execl(sys.executable, sys.executable, *sys.argv)

if __name__=="__main__":
        # Enter into a while loop to recieve commands from client
        print("\n\nWaiting for instruction")
        data = conn.recv(BUFFER_SIZE)
        print("\nRecieved instruction: {}".format(data))
        # Check the command and respond correctly
        if data == "UPLD":
            upld()
        elif data == "LIST":
            list_files()
        elif data == "DWLD":
            dwld()
        elif data == "DELF":
            delf()
        elif data == "QUIT":
            quit()
        # Reset the data to loop
        data = None
