# Save as client.py 
# Message Sender
import os
import hashlib
from socket import *
from cryptography.fernet import Fernet


host = "127.0.0.1" # set to IP address of target computer
port = 8080
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
key = input("Enter the secret key: ")
f = Fernet(key)

def encrypt(plaintext):
    h = hashlib.md5(plaintext).hexdigest()

    print("Message hash: " + h)
   
    mmac = str(str(plaintext,'utf-8') + h).encode() 
    msg = f.encrypt(mmac)
    return msg

while True:
    data = str(input("Enter message to send or type 'exit': ")).encode()
    ciphertext = encrypt(data)
    UDPSock.sendto(ciphertext, addr)
    if data == b'exit':
        break
    if data == b'newkey':
        key = input("Enter the secret key: ")
        f = Fernet(key)
UDPSock.close()
os._exit(0)

