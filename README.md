## This project is made by Andaloussi Mohamed Fares and Mohamed Amine Guessmi
### This is a client-server project using python and socket library 

### Part 1 : UDP TCP Simple Server-Client

Functions to use UDP protocol use : 

```
socket(socket.AF_INET, socket.SOCK_DGRAM) -> socket
```
```
socket.bind((HOST, PORT))
```
```
socket.sendto(byte(message),tuple(HOST,PORT))
```
```
socket.recvfrom(size)
```

Functions to use TCP protocol use :
```
socket(socket.AF_INET, socket.SOCK_STREAM) -> socket
```
```
socket.bind((HOST, PORT))
```
```
socket.listen()
```
```
socket.accept() -> (connection,address)
```
```
socket.connect((HOST, PORT))
```
```
connetion.sendall(byte(message))
```
```
connection.recv(size) -> data[byte]
```
### part 2 : finger 
In computer networking, the Name/Finger protocol and the Finger user information protocol are simple network protocols for the exchange of human-oriented status and user information.
port number on etc/services : 79/TCP

To start a service from etc/init.d 
```
sudo service [service_name] start 
``` 
or 
```
sudo systemctl [service_name] start 
```

