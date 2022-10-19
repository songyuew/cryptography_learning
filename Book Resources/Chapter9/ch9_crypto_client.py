# Message Sender - ch9_crypto_telnet_client.py
import hashlib, random, os, time
from binascii import hexlify
from socket import *
import Chapter9.ch9_crypto_telnet as ct

clientDH = clientDH = ct.gen_client_DH()
clientSecret = 0;

def get_dh_sharedsecret():
    key = int(open('server_public_dh_key.pem').read())
    clientDH.generateSharedKey(key)
    clientDH.getSharedKey()

    clientDH.generateSharedKey(key)

    shared_key = clientDH.sharedSecret

    return (shared_key)

def get_dh_sharedkey():
    key = int(open('server_public_dh_key.pem').read())
    clientDH.generateSharedKey(key)
    clientDH.getSharedKey()

    clientDH.generateSharedKey(key)

    private_key = clientDH.key

    return private_key
   
def encrypt(plaintext, usePKI, useDH, clientSecret):
    msg = ct.encrypt(plaintext, usePKI, useDH, clientSecret)
    return msg

def main():
    host = "127.0.0.1" # set to IP address of target computer
    port = 8080
    addr = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)

    # initiate the encryption variables
    sendUsingPrivate = False;
    sendUsingDH = False;
    skipEncryption = False;
    
    # no matter what, get the ECC shared key, only use it if the user enables
    clientSecret = get_dh_sharedkey()
    
    print ("Welcome to Crypto-Telnet! \n")
    print ("    Enable PKI: type 'addPKI'")
    print ("    Disable PKI: type 'removePKI'")
    print ("    Enable Diffie-Hellman: type 'addDH'")
    print ("    Disable Diffie-Hellman: type 'removeDH'")
    print ()
   
    # sending loop
    while True:
        if sendUsingPrivate == True or sendUsingDH == True:
            data = str(input("Enter secure message to send or type 'exit': ")).encode()
        else:
            data = str(input("Enter message to send or type 'exit': ")).encode()
        
        # determine if the user initiated a special command
        result = ct.check_client_command(data)
        # handle any custom commands
        if data == b'exit':
            break
        if result == 0:
            break
        if result == 10:
            sendUsingPrivate = False;
        if result == 11:
            sendUsingPrivate = True;
            skipEncryption = True;
        if result == 20:
            sendUsingDH = False;
        if result == 21:
            sendUsingDH = True;
            skipEncryption = True;


        ciphertext = encrypt(data, sendUsingPrivate, sendUsingDH, clientSecret)
        if skipEncryption:
            ciphertext = data;
            skipEncryption = False;

        # send the packet over UDP
        UDPSock.sendto(ciphertext, addr)

    # close UDP connection
    UDPSock.close()
    os._exit(0)

if __name__ == '__main__': 
	main() 


