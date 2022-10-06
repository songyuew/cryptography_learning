
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
message = b'To be encrypted'
key = RSA.importKey(open('public_key.pem').read())
cipher = PKCS1_OAEP.new(key)
ciphertext = cipher.encrypt(message)
print (ciphertext)
key = RSA.importKey(open('private_key.pem').read())
cipher = PKCS1_OAEP.new(key)
plaintext = cipher.decrypt(ciphertext)
print (plaintext)