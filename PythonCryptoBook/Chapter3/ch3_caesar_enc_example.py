key = 'abcdefghijklmnopqrstuvwxyz'
def enc_caesar(n, plaintext):
    result = ''
    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l
    return result.lower()

plaintext = 'We hold these truths to be self-evident, that all men are created equal.'
ciphertext = enc_caesar(3, plaintext)
print (ciphertext)
