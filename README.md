# This project is made by Andaloussi Mohamed Fares and Mohamed Amine Guessmi
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
Pass the host and the login to the fingerclient 
```
python3 ./fingerclient.py --login root --host 127.0.0.1
```
### part 3 : RPC 
server side 
```
rfoo.InetServer(MyHandler).start()
```
client side 
```
c = rfoo.InetConnection().connect()
rfoo.Proxy(c).add(2,3)
```
Note : rfoo library is deprecated 

### Part 4FTP File Server via Socket Programming in Python

To run the server/client, call the appropriate program from the terminal. Each program will display a short message on startup:
```
> python server.py

Welcome to the FTP server.

To get started, connect a client.
```
```
> python client.py

Welcome to the FTP client.

Call one of the following functions:
CONN           : Connect to server
UPLD file_path : Upload file
LIST           : List files
DWLD file_path : Download file
DELF file_path : Delete file
QUIT           : Exit

Enter a command:
```
As indicated, the first thing that needs to be done is to connect the client to the server. To do this, just enter the command CONN:
```
Enter a command: CONN
```
The client will then attempt a connection. If successful a message will appear:
```
Enter a command: Connect

Sending a server request...
Connection successful
```
After that, all other commands can be entered through the client. Messages will display the progress of the request on both the client and server end. For example, to upload a file 'my_file.mp4', use the following command:
```
Enter a command: UPLD my_file.mp4
```

When the server receives a file, it puts it in the same folder that it is in. Likewise, when the LIST command is used the server searches for files in the same folder that it is located in.

### Part 5 : Twitter API 

We can use Requests library to make get and post requests
Request (REQ) to the twitter API using the URI given 
Headers (HEADERS) are the authorization setting (OAuth2 / OAuth1.0a) 
```
response = requests.get(REQ,headers=HEADERS)
```
Now we need to deserialize the response (json format) so that it becomes a python object
```
response_deserialized = json.loads(response.text) 
```
