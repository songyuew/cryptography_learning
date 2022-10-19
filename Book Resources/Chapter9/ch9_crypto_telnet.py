# Telnet Encryption Helper - ch9_crypto_telnet.py
import os, base64, json
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.PublicKey import RSA, ECC
import Chapter9.ch9_diffiehellman as dh
from binascii import hexlify, unhexlify
from base64 import b64encode, b64decode

# encryption method used by all calls
def encrypt(message, usePKI, useDH, dhSecret):
    if usePKI == True:
        message = encrypt_rsa(message)
    if useDH == True:
        message = encrypt_dh(message, dhSecret)
    return message

# decryption method used by all calls
def decrypt(message, usePKI, useDH, dhSecret):
    if useDH == True:
        message = decrypt_dh(message, dhSecret)
    if usePKI == True:
        message = decrypt_rsa(message)
    return message

# delete all generated DH certs
def remove_dh_certs():
    try:
        os.remove("client_private_dh_key.pem")
        os.remove("client_public_dh_key.pem")
        os.remove("server_private_dh_key.pem")
        os.remove("server_public_dh_key.pem")
    except:
        return 0

# delete all generated RSA certs
def remove_rsa_certs():
    try:
        os.remove("client_private_key.pem")
        os.remove("client_public_key.pem")
    except:
        return 0

# generate Diffie-Hellman certificates for client
def gen_client_DH():
    clientDH =  dh.DiffieHellman(2,17,1024)
    
    privateKey = str(clientDH.privateKey).encode()
    fd = open("client_private_dh_key.pem", "wb")
    fd.write(privateKey)
    fd.close()

    publicKey = str(clientDH.publicKey).encode()
    fd = open("client_public_dh_key.pem", "wb")
    fd.write(publicKey)
    fd.close()

    clientDHSet = clientDH
    return clientDH

# generate Diffie-Hellman certificates for server
def gen_server_DH():

    svrDH =  dh.DiffieHellman(2,17,1024)

    privateKey = str(svrDH.privateKey).encode()
    fd = open("server_private_dh_key.pem", "wb")
    fd.write(privateKey)
    fd.close()

    publicKey = str(svrDH.publicKey).encode()
    fd = open("server_public_dh_key.pem", "wb")
    fd.write(publicKey)
    fd.close()

    key = (open('server_public_dh_key.pem').read())

    serverDHSet = svrDH
    return svrDH

# generate RSA certs
def gen_rsa_certs():
    #ch8_Generate_RSA_Certs.py
    from Crypto.PublicKey import RSA

    #Generate a public/ private key pair using 4096 bits key length (512 bytes)
    new_key = RSA.generate(4096, e=65537)

    #The private key in PEM format
    private_key = new_key.exportKey("PEM")

    #The public key in PEM Format
    public_key = new_key.publickey().exportKey("PEM")

    fd = open("client_private_key.pem", "wb")
    fd.write(private_key)
    fd.close()

    fd = open("client_public_key.pem", "wb")
    fd.write(public_key)
    fd.close()

# decrypt using RSA
def decrypt_rsa(ciphertext):
    key = RSA.importKey(open('client_private_key.pem').read())
    cipher = PKCS1_OAEP.new(key)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

# encrypt using RSA
def encrypt_rsa(message):
    key = RSA.importKey(open('client_public_key.pem').read())
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(message)

    plaintext = decrypt_rsa(ciphertext)

    return ciphertext

# encrypt using Diffie-Hellman - ECC
def encrypt_dh(plaintext, dhSecret):
    # encrypt using the shared secret from Client (Private) and Server (Public)
    ciphertext = encrypt_AES_GCM(plaintext,dhSecret)
    ciphertext = ciphertext.encode()
    #reverse = decrypt_AES_GCM(ciphertext, dhSecret)
    return ciphertext

# decrypt using Diffie-Hellman - ECC
def decrypt_dh(ciphertext, dhSecret):
    # decrypt using the shared secret from Client (Private) and Server (Public)
    ciphertext = ciphertext.decode('utf-8')
    plaintext = decrypt_AES_GCM(ciphertext,dhSecret)
    #reverse = encrypt_AES_GCM(ciphertext, dhSecret)
    return plaintext

# generate ECC certs
def gen_ecc_certs():
    key = ECC.generate(curve='P-256')
    f = open('myprivatekey.pem','wt')
    f.write(key.export_key(format='PEM'))
    f.close()
    f = open('myprivatekey.pem','rt')
    key = ECC.import_key(f.read())
    print (key)

# encrypt using AES-GCM
def encrypt_AES_GCM(msg, secretKey):
    aesCipher = AES.new(secretKey, AES.MODE_GCM)
    ct, authTag = aesCipher.encrypt_and_digest(msg)

    ct = hexlify(ct)
    ct = ct.decode('utf-8')
    authTag = hexlify(authTag)
    authTag = authTag.decode('utf-8')
    noncea = hexlify(aesCipher.nonce)
    nonce = noncea.decode('utf-8')
    
    ciphertext = json.dumps({'nonce':nonce, 'ciphertext':ct, 'tag':authTag})

    return ciphertext

# decrypt using AES-GCM
def decrypt_AES_GCM(encryptedMsg, secretKey):
   
    b64 = json.loads(encryptedMsg)
    
    nonce = str(b64['nonce'])
    nonce = nonce.encode()
    nonce = unhexlify(nonce)
    
    ct = str(b64['ciphertext'])
    ct = ct.encode()
    ct = unhexlify(ct)

    authTag = str(b64['tag'])
    authTag = authTag.encode()
    authTag = unhexlify(authTag)
    
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    nonce = b64encode(aesCipher.nonce).decode('utf-8')
    plaintext = aesCipher.decrypt_and_verify(ct, authTag)
    return plaintext
   
# encrypt using AES-CTR
def encrypt_AES_CTR(msg, secretKey):
    cipher = AES.new(secretKey, AES.MODE_CTR)
    ct_bytes = cipher.encrypt(msg)
    nonce = b64encode(cipher.nonce).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    ciphertext = json.dumps({'nonce':nonce, 'ciphertext':ct})
    return ciphertext

# decrypt using AES-CTR
def decrypt_AES_CTR(msg, secretKey):
    b64 = json.loads(msg)
    nonce = b64decode(b64['nonce'])
    ct = b64decode(b64['ciphertext'])
    cipher = AES.new(secretKey, AES.MODE_CTR, nonce=nonce)
    plaintext = cipher.decrypt(ct)
    return plaintext

# check client commands
def check_client_command(data):
    if data == b'addPKI':
        gen_rsa_certs()
        return 11
    elif data == b'removePKI':
        usePKI = False
        #ch9_remove_rsa_certs()
        return 10
    elif data == b'addDH':
        return 21
    elif data == b'removeDH':
        usePKI = False
        #ch9_remove_rsa_certs()
        return 20
    return 1

# check server commands
def check_server_command(data):
    if data == b'addPKI':
        return 11
    if data == b'removePKI':
        useDH = False
        return 10
    if data == b'addDH':
        return 21
    if data == b'removeDH':
        useDH = False
        return 20
    return 1

        

