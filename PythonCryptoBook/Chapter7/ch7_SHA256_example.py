import binascii, hashlib
k = b"secretkey"
msg = b"our secret message"
kplus = k + b"\x00"*(64-len(k))
ipad = b"\x36"*64
opad = b"\x5C"*64

def XOR(raw1, raw2):
    return binascii.unhexlify(format(int(binascii.hexlify(raw1), 16) ^

int(binascii.hexlify(raw2), 16), 'x'))
tag = hashlib.sha256(XOR(kplus, opad) + hashlib.sha256(XOR(kplus, ipad) + msg).digest()).digest()
print(binascii.hexlify(tag))
