
# Extended Euclidean Algorithm for finding modular inverse 
# eg: modinv(7, 26) = 15 
def egcd(a, b): 
    x,y, u,v = 0,1, 1,0
    while a != 0: 
        q, r = b//a, b%a 
        m, n = x-u*q, y-v*q 
        b,a, x,y, u,v = a,r, u,v, m,n 
    gcd = b 
    return gcd, x, y 
  
def modinv(a, m): 
    gcd, x, y = egcd(a, m) 
    if gcd != 1: 
        return None  # modular inverse does not exist 
    else: 
        return x % m 
  
  
# affine cipher encryption function  
# returns the cipher text 
def encrypt(text, key): 
    ''' 
    E = (a * x + b) % 26 
    '''
    return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26)  
                  + ord('A')) for t in text.upper().replace(' ', '') ]) 
  
  
# affine cipher decryption function  
# returns original text 
def decrypt(cipher, key): 
    ''' 
    D = (a^-1 * (x - b)) % 26 
    '''
    return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1]))  
                    % 26) + ord('A')) for c in cipher ]) 
  
  
# Test the encrypt and decrypt functions 
def main(): 
    # declaring text and key 
    text = 'CODEBOOK'
    key = [17, 20] 
  
    # calling encryption function 
    encrypted_text = encrypt(text, key) 
  
    print('Encrypted Text: {}'.format(encrypted_text )) 
  
    # calling decryption function 
    print('Decrypted Text: {}'.format
    (decrypt(encrypted_text, key) )) 
  
  
if __name__ == '__main__': 
    main() 
