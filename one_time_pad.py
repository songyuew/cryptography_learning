import binascii

def xorKey(secret):
    secret = secret.encode()
    # convert each character in a string to ASCII value in hex and concat
    hexstr = binascii.hexlify(secret)
    # convert the entire hex string to an integer
    key = int(hexstr,16)
    print(f"key: {key}")
    return key

def xorEnc(msg,key):
    msg = msg.encode()
    hexstr = binascii.hexlify(msg)
    print(f"hexstr: {hexstr.decode()}")
    # XOR
    ciphertext = int(hexstr,16) ^ key
    print(f"ciphertext: {ciphertext}")
    return ciphertext

def xorDec(msg,key):
    xorMsgKey = msg ^ key
    # convert integer to hex string
    back2hex = format(xorMsgKey, "x")
    print(f"back2hex: {back2hex}")
    evenpad = ("0" * (len(back2hex) % 2)) + back2hex
    plaintext = binascii.unhexlify(evenpad)
    print(f"plaintext: {plaintext.decode()}")
    return plaintext

key = xorKey("password")
cipher = xorEnc("Hello World",key)
plain = xorDec(cipher,key)