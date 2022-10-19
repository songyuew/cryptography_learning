# Save as ch7_e_server2.py 
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
        mmac = f.decrypt(ciphertext)
        mlen = len(mmac)
        m = (mmac[0:mlen - 32])
        h = (mmac[-32:])
        msg = m,h
    except:
        msg = ciphertext
    return msg

while True:
    (data, addr) = UDPSock.recvfrom(buf)
    
    plaintext = decrypt(data)

    h = hashlib.md5(plaintext[0])
    msg = str(plaintext[0], 'utf-8')
    hash = str(plaintext[1], 'utf-8')
    print ("Received message: " + msg)
    print ("Received digest: " + hash)
    print ("Calculated digest: " + h.hexdigest())

    if msg == "exit":
        break
    if msg == 'newkey':
        key = Fernet.generate_key()
        f = Fernet(key)
        print ("The key is :", str(key, 'utf-8'))

UDPSock.close()
os._exit(0)


