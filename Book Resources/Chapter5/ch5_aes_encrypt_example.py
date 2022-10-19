from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii, os
import random
data = b"secret"
key = binascii.hexlify(os.urandom(16))
iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
#print ('key: ', [x for x in key] )
#print()
cipher = AES.new(key, AES.MODE_CBC)
ct_bytes = cipher.encrypt(pad(data, AES.block_size))
ct = b64encode(ct_bytes).decode('utf-8')
print('iv: {}'.format(iv))
print()
print('ciphertext: {}'.format(ct))
print()
