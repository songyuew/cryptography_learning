def text2int(msg):
    print (msg)
    # convert string to hex
    
    hexstr = msg.encode("utf-8").hex()
    
    print (hexstr)
    # convert hex to integer
    integer_m = int(hexstr, 16)
    print (integer_m)
    # convert integer back to hex
    back2hex = format(integer_m, 'x')
    print (back2hex)
    # convert back to string
    evenpad = ('0' * (len(back2hex) % 2)) + back2hex
    
    import codecs
    plaintext = codecs.decode(evenpad, 'hex')

    print (plaintext)

text2int("Hello World")
