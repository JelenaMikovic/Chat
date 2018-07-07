import socket
import time

host = '127.0.0.1'
port = 5000
clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)
print "Server Started."
while True:
    try:
        message, addr = s.recvfrom(1024)
        if addr not in clients:
            clients.append(adresa)
        for client in clients:
            s.sendto(message, client)
    except:
        pass
