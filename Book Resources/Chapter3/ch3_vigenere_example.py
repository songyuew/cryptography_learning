def key_vigenere(key):
    keyArray = []
    for i in range(0,len(key)):
        keyElement = ord(key[i]) - 65
        keyArray.append(keyElement)
    return keyArray

def shiftEnc(c, n):
    return chr(((ord(c) - ord('A') + n) % 26) + ord('a'))


def enc_vigenere(plainttext, key):
    secret = "".join([shiftEnc(plainttext[i], key[i % len(key)]) for i
    in range(len(plainttext))])
    return secret

def shiftDec(c, n):
    c = c.upper()
    return chr(((ord(c) - ord('A') - n) % 26) + ord('a'))

def dec_vigenere(ciphertext, key):
    plain = "".join([shiftDec(ciphertext[i], key[i % len(key)]) for i in
    range(len(ciphertext))])
    return plain

secretKey = 'DECLARATION'
key = key_vigenere(secretKey)
plaintext = 'ALL MEN ARE CREATED EQUAL'
ciphertext = enc_vigenere(plaintext, key)
print(ciphertext)
decoded = dec_vigenere(ciphertext, key)
print(decoded)