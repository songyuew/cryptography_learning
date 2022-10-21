# DES is no longer secured, use 3DES instead
from Crypto.Cipher import DES 

key = b'shhhhhh!' 
origText = b'The US Navy has submarines in Kingsbay!!' 

des = DES.new(key, DES.MODE_ECB) 
ciphertext = des.encrypt(origText) 
plaintext = des.decrypt(ciphertext) 

print('The original text is {}'.format(origText)) 
print('The ciphertext is {}'.format(ciphertext)) 
print('The plaintext is {}'.format(plaintext)) 
print()