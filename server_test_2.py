'''
WARNING
You must disable the firewall for the network you are on for clients to access your server.

Most Wifi networks, including your home wifi network, are classified as public networks.
In Windows Security, under Firewall and Network Protection, click on "Domain network",
"Private network", and/or "Public network" to see which type of network your current internet
access falls under.

In my experience, allowing a port through the firewall is insufficient.
'''

'''
try without the HisSocket class
'''

'''
again, code from
https://docs.python.org/3/howto/sockets.html
https://www.geeksforgeeks.org/socket-programming-python/
'''

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 7777 #just a random port I make for this
serversocket.bind((socket.gethostname(), port))
#use socket.gethostname() to accept any IP address
#'' and '0.0.0.0' only work on local networks

#socket.gethostname() returns 'DESKTOP-GO1JE2E' on my device . . .
my_IP = socket.gethostbyname(socket.gethostname())
print(f"Your IP address is {my_IP}")
#print(f"your IP is of data type {type(my_IP)}") #ip addresses are just strings

serversocket.listen(5) #well, both tutorials used a max of 5 connections, so why not?

message = "Test"
message2 = message.encode("utf-8")
print(message2)
print(len(message2))

while True:
    (clientsocket, address) = serversocket.accept()

    print(f"connection made with {address}")

    clientsocket.send(message2)
