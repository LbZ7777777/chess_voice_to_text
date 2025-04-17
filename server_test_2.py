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
serversocket.bind(("0.0.0.0", port)) #use "0.0.0.0" to accept any IP address

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