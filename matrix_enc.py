from operator import inv
from pydoc import plain
import numpy as npy

# this is a symmetric key encryption
key_size = int(input("Key size (square matrix): "))
enc_matrix = npy.random.rand(key_size,key_size)
print("--------------------KEY-----------------------")
print(enc_matrix)
npy.save("key_matrix.npy",enc_matrix)

msg = input("Message to encrypt: ")

# pad if necessary
if (len(msg) % key_size != 0):
    msg += " " * (key_size - len(msg) % key_size)

# convert to integers (ASCII)
ascii = []
for char in msg:
    ascii.append(ord(char))

# create numpy array on plaintext
rowLen = int(len(ascii) / key_size)
plaintext = []
for r in range(key_size): 
    plaintext.append(ascii[r*rowLen:(r+1)*rowLen])

plaintext_matrix = npy.array(plaintext)
print("--------------------PLAINTEXT-----------------")
print(plaintext_matrix)

# encrypt to cipher matrix
cipher = enc_matrix @ plaintext_matrix
print("--------------------CIPHER--------------------")
print(cipher)
npy.save("cipher_matrix.npy",cipher)

# get decryption key, which is the inverse of encryption matrix
dec_matrix = npy.linalg.inv(enc_matrix)
decrypted_matrix = dec_matrix @ cipher

# convert decrypted matrix back to characters
decrypted_string = ""
decrypted_list = []
for row in decrypted_matrix:
    decrypted_list.extend(row)
for num in decrypted_list:
    decrypted_string += chr(round(num))

print("--------------------PLAINTEXT-----------------")
print(decrypted_string)