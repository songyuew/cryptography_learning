def RC4(data,key):
    # mass up all numbers in box (create randomness determined by user input key)
    # adding randomness to initial vector
    x = 0 
    box = range(256) 
    for i in range(256): 
        x = (x + box[i] + ord(key[i % len(key)])) % 256 
        # swap range objects 
        box = list(box) 
        box[i], box[x] = box[x], box[i] 
        
    # print(box)
    # print(len(box))
    x = 0
    y = 0
    out = []
    
    # generation of key stream
    # use prepared key to XOR with data bit by bit
    for char in data:
        x = (x + 1) % 256
        y = (y + box[x]) % 256
        box[x],box[y] = box[y],box[x]
        out.append(chr(ord(char) ^ box[(box[x]+box[y]) % 256]))
    
    return "".join(out)
    
cipher = RC4("sample data sample data sample data","secretkey2")
print(cipher)
plaintext = RC4(cipher,"secretkey2")
print(plaintext)