import sys
import numpy as np

def cipher_encryption(plain, key):

    # if message length is an odd number, place a zero at the end.
    len_chk = 0
    if len(plain) % 2 != 0:
        plain += "0"
        len_chk = 1
        
    # msg to matrices
    row = 2
    col = int(len(plain)/2)
    msg2d = np.zeros((row, col), dtype=int)
    
    itr1 = 0
    itr2 = 0
    for i in range(len(plain)):
        if i%2 == 0:
            msg2d[0][itr1]= int(ord(plain[i]) - 65)
            itr1 += 1
        else:
            msg2d[1][itr2] = int(ord(plain[i]) - 65)
            itr2 += 1
    
    
    # key to 2x2
    key2d = np.zeros((2,2), dtype=int)
    itr3 = 0
    for i in range(2):
        for j in range(2):
            key2d[i][j] = ord(key[itr3]) - 65
            itr3 += 1
            
    print (key2d)
            
    # checking validity of the key
    # finding determinant
    deter = key2d[0][0] * key2d[1][1] - key2d[0][1] * key2d[1][0]
    deter = deter % 26
    
    # finding multiplicative inverse
    for i in range(26):
        temp_inv = deter * i
        if temp_inv % 26 == 1:
            mul_inv = i
            break
        else:
            continue
    
    if mul_inv == -1:
        print("Invalid key")
        sys.exit()
    
    encryp_text = ""
    itr_count = int(len(plain)/2)
    if len_chk == 0:
        for i in range(itr_count):
            temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
            encryp_text += chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
            encryp_text += chr((temp2 % 26) + 65)
    else:
        for i in range(itr_count-1):
            temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
            encryp_text += chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
            encryp_text += chr((temp2 % 26) + 65)
    
    print("Encrypted text: {}".format(encryp_text))
    return encryp_text
    
def cipher_decryption(cipher, key):

    # if message length is an odd number, place a zero at the end.
    len_chk = 0
    if len(cipher) % 2 != 0:
        cipher += "0"
        len_chk = 1
        
    # msg to matrices
    row = 2
    col = int(len(cipher)/2)
    msg2d = np.zeros((row, col), dtype=int)
    
    itr1 = 0
    itr2 = 0
    for i in range(len(cipher)):
        if i%2 == 0:
            msg2d[0][itr1]= int(ord(cipher[i]) - 65)
            itr1 += 1
        else:
            msg2d[1][itr2] = int(ord(cipher[i]) - 65)
            itr2 += 1

    
    # key to 2x2
    key2d = np.zeros((2,2), dtype=int)
    itr3 = 0
    for i in range(2):
        for j in range(2):
            key2d[i][j] = ord(key[itr3]) - 65
            itr3 += 1

    # finding determinant
    deter = key2d[0][0] * key2d[1][1] - key2d[0][1] * key2d[1][0]
    deter = deter % 26

    # finding multiplicative inverse
    for i in range(26):
        temp_inv = deter * i
        if temp_inv % 26 == 1:
            mul_inv = i
            break
        else:
            continue
    
    # adjugate matrix
    # swapping
    key2d[0][0], key2d[1][1] = key2d[1][1], key2d[0][0]
    
    #changing signs
    key2d[0][1] *= -1
    key2d[1][0] *= -1
    
    key2d[0][1] = key2d[0][1] % 26
    key2d[1][0] = key2d[1][0] % 26
    
    # multiplying multiplicative inverse with adjugate matrix
    for i in range(2):
        for j in range(2):
            key2d[i][j] *= mul_inv
    
    # modulo
    for i in range(2):
        for j in range(2):
            key2d[i][j] = key2d[i][j] % 26
            
    # cipher to plaintext
    decryp_text = ""
    itr_count = int(len(cipher)/2)
    if len_chk == 0:
        for i in range(itr_count):
            temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
            decryp_text += chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
            decryp_text += chr((temp2 % 26) + 65)
        # for
    else:
        for i in range(itr_count-1):
            temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
            decryp_text += chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
            decryp_text += chr((temp2 % 26) + 65)
        # for
    # if else
    
    print("Decrypted text: {}".format(decryp_text))
    
plaintext = "Secret Message"
plaintext = plaintext.upper().replace(" ","")
key = "hill"
key = key.upper().replace(" ","")
ciphertext = cipher_encryption(plaintext, key)
cipher_decryption(ciphertext, key)
#Encrypted text: CIUBYTMUKGWO
#Decrypted text: SECRETMESSAG
