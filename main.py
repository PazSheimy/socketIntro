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








