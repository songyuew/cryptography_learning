import os
from chacha20poly1305 import ChaCha20Poly1305

# generate a random key that has 32 bits
key = os.urandom(32)

print('The key that will be used is {}'.format(key))
print()
plaintext = b'Attack the yellow submarine.'
print('The plaintext is {}'.format(plaintext))
print()

# generate a random IV that has 12 bits
iv = os.urandom(12)
cip = ChaCha20Poly1305(key)

ciphertext = cip.encrypt(iv, plaintext)
print(ciphertext)
print()

plaintext = cip.decrypt(iv, ciphertext)
print(plaintext)
print()


