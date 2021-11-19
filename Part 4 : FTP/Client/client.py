import socket
import sys
import os
import struct

# Initialise socket stuff
TCP_IP = "127.0.0.1" # Only a local server
TCP_PORT = 1423 # Just a random choice
BUFFER_SIZE = 1024 # Standard chioce
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def conn():
    # Connect to the server
    print("Sending server request...")
    try:
        s.connect((TCP_IP, TCP_PORT))
        print("Connection sucessful")
    except:
        print("Connection unsucessful. Make sure the server is online.")

def upld(file_name):
    return

def list_files():
    return


def dwld(file_name):
    # Download given file
    print("Downloading file: {}".format(file_name))
    try:
        # Send server request
        s.send(file_name.encode())
    except:
        print("Couldn't make server request. Make sure a connection has bene established.")
        return

    try:
        with open(file_name, 'wb') as f:
            while True:
                print('receiving data...')
                data = s.recv(1024)
                print('data=%s', (data))
                if not data:
                    break
                # write data to a file
                f.write(data)

    except:
        print("Error downloading file")
        return
    return


def delf(file_name):
    return

def quit():
    s.send("QUIT")
    # Wait for server go-ahead
    s.recv(BUFFER_SIZE)
    s.close()
    print("Server connection ended")
    return

print("\n\nWelcome to the FTP client.\n\nCall one of the following functions:\nCONN           : Connect to server\nUPLD file_path : Upload file\nLIST           : List files\nDWLD file_path : Download file\nDELF file_path : Delete file\nQUIT           : Exit")

while True:
    # Listen for a command
    prompt = input("\nEnter a command: ")
    if prompt[:4].upper() == "CONN":
        conn()
    elif prompt[:4].upper() == "UPLD":
        upld(prompt[5:])
    elif prompt[:4].upper() == "LIST":
        list_files()
    elif prompt[:4].upper() == "DWLD":
        dwld(prompt[5:])
    elif prompt[:4].upper() == "DELF":
        delf(prompt[5:])
    elif prompt[:4].upper() == "QUIT":
        quit()
        break
    else:
        print("Command not recognised; please try again")
