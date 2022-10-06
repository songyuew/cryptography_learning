import socket
import sys
import hashlib
from _thread import *

host = 'localhost'
port = 5555
print (host, port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))

s.listen(5)

def threaded_client(conn):

    conn.send(str.encode('Welcome, type your info\n'))

    while True:
        data = conn.recv(2048)

        h = hashlib.md5(data)


        reply = 'Server output: '+ data.decode('utf-8') + '\n'
        reply += 'The MD5 for the message is: ' + h.hexdigest() + '\n'
        
        
        if not data:
            break
        conn.sendall(str.encode(reply))
    conn.close()


while True:
    conn, addr = s.accept()
    print('connected to: ' +addr[0] + ':' + str(addr[1]))
    print (s)
    start_new_thread(threaded_client, (conn,))

