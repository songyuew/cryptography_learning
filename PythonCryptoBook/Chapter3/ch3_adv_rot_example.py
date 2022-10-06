key = 'abcdefghijklmnopqrstuvwxyz'

def enc_dec_ROT13(n, plaintext):
    result = ''
    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l
    return result.lower()


plaintext = 'We hold these truths to be self-evident, that all men are created equal.'
ciphertext = enc_dec_ROT13(13, plaintext)
print (ciphertext)
plaintext = enc_dec_ROT13(13, ciphertext)
print (plaintext)
