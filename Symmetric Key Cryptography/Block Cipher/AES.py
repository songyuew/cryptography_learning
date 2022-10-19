import os
import binascii
import random

# generate strong 16 bytes AES key
key = binascii.hexlify(os.urandom(16))
print(key)

# the initial vector need to be different for each message, however, it has low security
# requirement and can be generated with random module, send with cipher in plain text.
iv = ''.join([chr(random.randint(0,255)) for i in range(16)])
print(iv)

# to be continued