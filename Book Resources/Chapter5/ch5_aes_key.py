import os
import binascii
key = binascii.hexlify(os.urandom(16))
print ('key', [x for x in key] )
