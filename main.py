import socket

# File to show cross-platform
# create a local "echo" server

'''
pyip = socket.gethostbyname('www.python.org')
print(f"python's ip is {pyip}")
HOST = socket.gethostbyname('localhost')
print(f"our localhost ip is {HOST}")
'''
"""
# Host = localhost ip, port = arbitray number over 1023
HOST = socket.gethostbyname('localhost')
PORT = 12345
print(f"our localhost ip is {HOST} an port is {PORT}")

# create a socket "instance" (object)
simple = socket.socket()
print("socket created successfully")
# Bind to a port
#simple.bind('', PORT) # if lisent to nothing-> ('') it would listen to all hosts
#if bind(HOST, port) it will keep it local and listen to our local host
simple.bind((HOST, PORT))
print(f"Socket is bimded to {PORT}")
#once bound we must "listen"
simple.listen(5)
# infinite loop - until interrupt or error
while True:

# Establish connection
    conn, addr = simple.accept()
    print(f"Connection accepted from {addr}")

    #send message confirming connection
    conn.send("you were successfully connected".encode())

# we're closing after a single person send event and then disconnecting (no infinite loop)
    conn.close()
    break
"""
#create a socket object
sclient = socket.socket()

#cross-platform, telnet-ish connection
PORT = 12345
HOST = socket.gethostbyname('localhost')

#in order to connect to a server - i must connect to its socket
sclient.connect((HOST, PORT))

#receive some data from our connected cleints (decode that string)
print(sclient.recv(1024).decode())
#close connection
sclient.close()

""" Chatclient
import time, socket, sys
print('Client Server...')
time.sleep(1)
#Get the hostname, IP Address from socket and set Port
soc = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
#get information to connect with the server
print(shost, '({})'.format(ip))
server_host = input('Enter server\'s IP address:')
name = input('Enter Client\'s name: ')
port = 12345
print('Trying to connect to the server: {}, ({})'.format(server_host, port))
time.sleep(1)
soc.connect((server_host, port))
print("Connected...\n")
soc.send(name.encode())
server_name = soc.recv(1024)
server_name = server_name.decode()
print('{} has joined...'.format(server_name))
print('Enter [bye] to exit.')
while True:
    message = soc.recv(1024)
    message = message.decode()
    print(server_name, ">", message)
    message = input(str("Me > "))
    
    if message == "[bye]":
        message = "Leaving the Chat room"
        soc.send(message.encode())
        print("\n")
        break
    soc.send(message.encode())"""

"""Chat server
import time, socket, sys
print('Setup Server...')
time.sleep(1) #remove?
#Get the hostname, IP Address from socket and set Port
soc = socket.socket()
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
port = 12345
soc.bind((host_name, port))
print(host_name, '({})'.format(ip))
#username
name = input('Enter name: ')
soc.listen(1) #Try to locate using socket
print('Waiting for incoming connections...')
connection, addr = soc.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")
print('Connection Established. Connected From: {}, ({})'.format(addr[0], addr[0]))
#get a connection from client side
client_name = connection.recv(1024)
client_name = client_name.decode()
print(client_name + ' has connected.')
print('Press [bye] to leave the chat room')
connection.send(name.encode())
while True:
    message = input('Me > ')
    if message == '[bye]':
        message = 'Good Night...'
        connection.send(message.encode())
        print("\n")
        break
    connection.send(message.encode())
    message = connection.recv(1024)
    message = message.decode()
    print(client_name, '>', message)"""

"""Client connect
import socket            
 
# Create a socket object
sclient = socket.socket()        
 
## cross-platform, telnet-ish connection
PORT = 12345
HOST = socket.gethostbyname("localhost")
# in order to "connect" to a server - I must "connect" to its socket
sclient.connect((HOST, PORT))
# recieve some data from our connected client (decode that string)
print(sclient.recv(1024).decode())
#close connection
sclient.close()
"""

"""Ex simple server
import socket
## File to show cross-platform.
## Create a local "echo" server
## HOST = localhost IP, PORT = arbitray number over 1023
HOST = socket.gethostbyname('localhost')
PORT = 12345
print(f"Our localhost ip is {HOST} and port is {PORT}")
## create a socket "instance" (object)
simple = socket.socket()
print("Socket created successfully")
## Bind to a port
simple.bind((HOST, PORT))
print(f"Socket is binded to {PORT}")
## once "bound" we must "listen"
simple.listen(5)
## infinte loop - until interrupt or error
while True:
    # Establish connection for our simple server
    conn, addr = simple.accept()
    print(f"Connection accepted from {addr}")
    # Send message confirming connection
    conn.send("You were successfully connected".encode())
    ## We're closing after a single send event and then disconnecting (no infinte 
loop)
    conn.close()
    break
"""

"""pingwithoutping
import socket
## File to show cross-platform.
HOST = socket.gethostbyname('localhost')
print(f"Our localhost ip is {HOST}")"""








