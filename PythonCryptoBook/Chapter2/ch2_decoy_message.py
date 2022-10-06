from binascii import hexlify, unhexlify

def otpSuperMsg(msg1, msg2):
    hex1 = hexlify(msg1)
    hex2 = hexlify(msg2)
    cipher1 = int(hex1, 16)
    cipher2 = int(hex2, 16)
    msg = cipher1 ^ cipher2
    return msg
    
def otpEnc(msg, key):
    superKey = int(msg, 16) ^ key
    return superKey
    
def otpDec(msg, key):
    xorMsgKey = msg ^ key
    back2hex = format(xorMsgKey, 'x') 
    evenpad = ('0' * (len(back2hex) % 2)) + back2hex
    plaintext = unhexlify(evenpad)
    return plaintext

realMessage = b"attackthematmidnight!"
decoyMessage= b"retreatanddonotattack"
msg = otpSuperMsg(realMessage, decoyMessage)

realMsg = hexlify(realMessage)
decoyMsg = hexlify(decoyMessage)
realKey = int(realMsg, 16) ^ msg
decoyKey = int(decoyMsg, 16) ^ msg

print ("The secret message is: ", msg)
print ("The real key is: ", realKey)
print ("The decoy key is: ", decoyKey)
print ()
# choose either the decoy key or the real key
key = realKey
plain = otpDec(msg, key)
print (plain)
print ()
key = decoyKey
plain = otpDec(msg, key)
print ()
print (plain)


