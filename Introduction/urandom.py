from os import urandom
import binascii

# get random hex string
# the prameter of urandom is the number of bytes to get
randomHex = binascii.hexlify(urandom(32)).decode()
# there should be 64 characters
print(randomHex)

# get integer
serial = int.from_bytes(urandom(20), byteorder="big")
print(serial)