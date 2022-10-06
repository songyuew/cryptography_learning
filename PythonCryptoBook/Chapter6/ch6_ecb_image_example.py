from Crypto.Cipher import AES
key = b"aaaabbbbccccdddd"
cipher = AES.new(key, AES.MODE_ECB)
# encrypt using ECB mode
with open("chapter6/ch6_secret_image.bmp", "rb") as f:
    byteblock = f.read()

pad = len(byteblock)%16 * -1
byteblock_trimmed = byteblock[64:pad]
ciphertext = cipher.encrypt(byteblock_trimmed)
ciphertext = byteblock[0:64] + ciphertext + byteblock[pad:]

with open("chapter6/e_ch6_secret_image.bmp", "wb") as f:
    f.write(ciphertext)

# decrypt using the reverse process
with open("chapter6/e_ch6_secret_image.bmp", "rb") as f:
    byteblock = f.read()

pad = len(byteblock)%16 * -1
byteblock_trimmed = byteblock[64:pad]
plaintext = cipher.decrypt(byteblock_trimmed)
plaintext = byteblock[0:64] + plaintext + byteblock[pad:]

with open("chapter6/d_ch6_secret_image.bmp", "wb") as f:
    byteblock = f.write(plaintext)

print ("done")
