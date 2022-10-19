from Crypto.Cipher import AES
iv = "1111222233334444"
key = "aaaabbbbccccdddd"

cipher = AES.new(key, AES.MODE_CBC, iv)
# encrypt using CBC mode
with open("chapter6/plane.bmp", "rb") as f:
    byteblock = f.read()

pad = len(byteblock)%16 * -1
byteblock_trimmed = byteblock[64:pad]
ciphertext = cipher.encrypt(byteblock_trimmed)
ciphertext = byteblock[0:64] + ciphertext + byteblock[pad:]

with open("chapter6/plane_cbc.bmp", "w") as f:
    f.write(ciphertext)

# decrypt using the reverse process

with open("chapter6/plane_cbc.bmp", "rb") as f:
    byteblock = f.read()

pad = len(byteblock)%16 * -1
byteblock_trimmed = byteblock[64:pad]
plaintext = cipher.decrypt(byteblock_trimmed)
plaintext = byteblock[0:64] + plaintext + byteblock[pad:]

with open("chapter6/dplane_cbc.bmp", "w") as f:
    byteblock = f.write(plaintext)
print ("done")
