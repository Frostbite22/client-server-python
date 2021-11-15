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
