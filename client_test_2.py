'''
removing HisSocket class

again, code from
https://docs.python.org/3/howto/sockets.html
https://www.geeksforgeeks.org/socket-programming-python/
'''

import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket made")
except socket.error as err:
    print(f"Socket not made; error: {err}")

port = 7777 #need to match ports with the server


host_ip = "127.0.0.1" #apparently what you use to connect locally
    #"192.168.0.5" #well . . . I know my IP address
    #for some url you'd go host_ip = socket.gethostbyname('url here')
    #btw shift + tab does the opposite of a tab


s.connect((host_ip, port))

data = s.recv(4)

print(data.decode("utf-8"))

