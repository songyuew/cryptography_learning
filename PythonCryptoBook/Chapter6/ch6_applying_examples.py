from Crypto.Cipher import AES
def Open_File(filename):
    with open(filename, "rb") as f:
        byteblock = f.read()
    return byteblock

def Save_File(filename, block):
    with open(filename,"wb") as f:
        f.write(block)

def Get_Padding(block):
    l = len(block) %16
    return (l * -1)


def Encrypt(cipher,read_filename, save_filename):
    block = Open_File(read_filename)
    pad = Get_Padding(block)
    block_trimmed = block[64:pad]
    ciphertext = cipher.encrypt(block_trimmed)
    ciphertext = block[0:64] + ciphertext + block[pad:]
    Save_File(save_filename, ciphertext)

def Decrypt(cipher,read_filename, save_filename):
    block = Open_File(read_filename)
    pad = Get_Padding(block)
    block_trimmed = block[64:pad]
    ciphertext = cipher.decrypt(block_trimmed)
    ciphertext = block[0:64] + ciphertext + block[pad:]
    Save_File(save_filename, ciphertext)

def Init_Cipher(key, mode, iv):
    cipher = AES.new(key, mode, iv)
    return cipher

# set the key and iv values
key = "aaaabbbbccccdddd"
iv = "1111222233334444"
# Available AES Block Modes
# AES.MODE_ECB = 1
# AES.MODE_CBC = 2
# AES.MODE_CFB = 3
# AES.MODE_OFB = 5
# AES.MODE_CTR = 6
# AES.MODE_OPENPGP = 7
mode = AES.MODE_CBC
c = Init_Cipher(key,mode, iv)
Encrypt(c, "plane.bmp", "eplane.bmp")
Decrypt(c, "eplane.bmp", "dplane.bmp")
