import binascii
def text2int(msg):
    print (msg)
    # convert string to hex
    #hexstr = msg.encode('hex')
    msg = msg.encode()
    hexstr = binascii.hexlify(msg)
    print (hexstr)
    # convert hex to integer
    integer_m = int(hexstr, 16)
    print (integer_m)
    # convert integer back to hex
    back2hex = format(integer_m, 'x')
    print (back2hex)
    # convert back to string
    evenpad = ('0' * (len(back2hex) % 2)) + back2hex
    #plaintext = evenpad.decode('hex')
    plaintext = binascii.unhexlify(evenpad)
    print (plaintext)

text2int("Hello World")
