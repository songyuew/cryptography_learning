import random


def Playfair_box_shift(i1, i2):
    r1 = i1/5
    r2 = i2/5
    c1 = i1 % 5
    c2 = i2 % 5
    out_r1 = r1
    out_c1 = c2
    out_r2 = r2
    out_c2 = c1
    if r1 == r2:
        out_c1 = (c1 + 1) % 5
        out_c2 = (c2 + 1) % 5
    elif c1 == c2:
        out_r1 = (r1 + 1) % 5
        out_r2 = (r2 + 1) % 5
    return out_r1*5 + out_c1, out_r2*5 + out_c2

def Playfair_enc(plain):
    random.shuffle(words)
    seed = "".join(words[:10]).replace('j','i')
    alpha = 'abcdefghiklmnopqrstuvwxyz'
    suffix = "".join( sorted( list( set(alpha) - set(seed) ) ) )
    seed_set = set()
    prefix = ""
    for letter in seed:
        if not letter in seed_set:
            seed_set.add(letter)
            prefix += letter
            key = prefix + suffix
            secret = ""
        for i in range(0,len(plain),2):
            chr1 = plain[i]
            chr2 = plain[i+1]
            if chr1 == chr2:
                chr2 = 'X'
            i1 = key.find(chr1.lower())
            i2 = key.find(chr2.lower())
            ci1, ci2 = Playfair_box_shift(i1, i2)
            secret += key[ci1] + key[ci2]
    return secret, key

def Playfair_box_shift_dec(i1, i2):
    r1 = i1/5
    r2 = i2/5
    c1 = i1 % 5
    c2 = i2 % 5
    out_r1 = r1
    out_c1 = c2
    out_r2 = r2
    out_c2 = c1
    if r1 == r2:
        out_c1 = (c1 - 1) % 5
        out_c2 = (c2 - 1) % 5
    elif c1 == c2:
        out_r1 = (r1 - 1) % 5
        out_r2 = (r2 - 1) % 5
    return out_r1*5 + out_c1, out_r2*5 + out_c2
    
def Playfair_dec(ciphertext, sharedkey):
    seed = "".join(sharedkey).replace('j','i')
    alpha = 'abcdefghiklmnopqrstuvwxyz'
    suffix = "".join( sorted( list( set(alpha) - set(seed) ) ) )
    seed_set = set()
    prefix = ""
    for letter in seed:
        if not letter in seed_set:
            seed_set.add(letter)
            prefix += letter
    
    key = prefix + suffix
    plaintext = ""
    for i in range(0,len(ciphertext),2):
        chr1 = ciphertext[i]
        chr2 = ciphertext[i+1]
        print (chr1, chr2)
        if chr1 == chr2:
            chr2 = 'X'
        i1 = key.find(chr1.lower())
        i2 = key.find(chr2.lower())
        ci1, ci2 = Playfair_box_shift_dec(i1, i2)
        plaintext += key[ci1] + key[ci2]
    
        return plaintext

originaltext = "Hello world."

ciphertext, key = Playfair_enc(originaltext)
plaintext = Playfair_dec(ciphertext,key)

print(ciphertext)
print(key)
print(plaintext)