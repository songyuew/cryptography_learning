
# Save as server.py 
# Message Receiver
import hashlib
import random
import os
from socket import *
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

print ("The key is :", str(key, 'utf-8'))
    
host = ""
port = 8080
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print ("Waiting to receive messages...")

def decrypt(ciphertext):
    try:
        msg = f.decrypt(ciphertext)
    except:
        msg = ciphertext
    return msg

while True:
    (data, addr) = UDPSock.recvfrom(buf)
    h = hashlib.md5(data)
    
    plaintext = decrypt(data)
    msg = str(plaintext, 'utf-8')
    print ("Received message: " + msg)
    if msg == "exit":
        break
    if msg == 'newkey':
        key = Fernet.generate_key()
        f = Fernet(key)
        print ("The key is :", str(key, 'utf-8'))

UDPSock.close()
os._exit(0)

