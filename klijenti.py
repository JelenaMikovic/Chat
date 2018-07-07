import socket
import threading
import time

loker = threading.Lock()
shutdown = False

def receving(name, sock):
    while not shutdown:
        try:
            loker.acquire()
            while True:
                data, adresa = sock.recvfrom(1024)
                print str
        except:
            pass
        finally:
            loker.release()

host = '127.0.0.1'
port = 0

server = ('127.0.0.1',5000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

rT = threading.Thread(target=receving, args=("RecvThread",s))
rT.start()

nadimak = raw_input("Name: ")
message = raw_input(nadimak + "-> ")
while message != 'q':
    if message != '':
        s.sendto(nadimak + ": " + message, server)
    loker.acquire()
    message = raw_input(nadimak + "-> ")
    loker.release()
    time.sleep(0.2)

shudown = True
rT.join()
s.close()

