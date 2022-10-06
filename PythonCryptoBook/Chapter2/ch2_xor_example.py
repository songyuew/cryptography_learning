import binascii

def xorKey(secret):
    secret = secret.encode()
    hexstr = binascii.hexlify(secret)
    key = int(hexstr, 16)
    print ("key: ", key)
    return key

def xorEnc(msg, key):
    msg = msg.encode()
    hexstr = binascii.hexlify(msg)
    print ("hexstr: ", hexstr)
    ciphertext = int(hexstr, 16) ^ key
    print ("ciphertext: ", ciphertext)
    return ciphertext

def xorDec(msg, key):
    xorMsgKey = msg ^ key
    back2hex = format(xorMsgKey, 'x')
    print ("back2hex: ", back2hex)
    evenpad = ('0' * (len(back2hex) % 2)) + back2hex
    plaintext = binascii.unhexlify(evenpad)
    print ("plaintext: ", plaintext)
    return plaintext

key = xorKey("mysecret")
key2 = xorKey("wrongpass")
cipher = xorEnc('Hello world',key)
plain = xorDec(cipher,key)
wrongplain = xorDec(cipher, key2)
