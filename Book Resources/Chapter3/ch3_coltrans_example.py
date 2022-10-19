
def cipher_encryption(plain_text, key):

    keyword_num_list = keyword_num_assign(key)
    num_of_rows = int(len(plain_text) / len(key))

    # break message into grid for key
    arr = [[0] * len(key) for i in range(num_of_rows)]
    z = 0

    for i in range(num_of_rows):
        for j in range(len(key)):
            arr[i][j] = plain_text[z]
            z += 1

    num_loc = get_number_location(key, keyword_num_list)

    cipher_text = ""
    k = 0
    for i in range(num_of_rows):
        if k == len(key):
            break
        else:
            d = int(num_loc[k])

        for j in range(num_of_rows):
            cipher_text += arr[j][d]
        k += 1
    return cipher_text

def get_number_location(key, keyword_num_list):
    num_loc = ""
    for i in range(len(key) + 1):
        for j in range(len(key)):
            if keyword_num_list[j] == i:
                num_loc += str(j)
    return num_loc

def keyword_num_assign(key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    keyword_num_list = list(range(len(key)))
    init = 0
    for i in range(len(alpha)):
        for j in range(len(key)):
            if alpha[i] == key[j]:
                init += 1
                keyword_num_list[j] = init
    return keyword_num_list

def print_grid(plain_text, key):

    keyword_num_list = keyword_num_assign(key)

    for i in range(len(key)):
        print(key[i], end = " ", flush=True)

    print()
    for i in range(len(key)):
        print(str(keyword_num_list[i]), end=" ", flush=True)
    print()
    print("-------------------------")

    # in case characters don't fit the entire grid perfectly.
    extra_letters = len(plain_text) % len(key)

    dummy_characters = len(key) - extra_letters

    if extra_letters != 0:
        for i in range(dummy_characters):
            plain_text += "."

    num_of_rows = int(len(plain_text) / len(key))

    # Converting message into a grid
    arr = [[0] * len(key) for i in range(num_of_rows)]
    z = 0

    for i in range(num_of_rows):
        for j in range(len(key)):
            arr[i][j] = plain_text[z]
            z += 1

    for i in range(num_of_rows):
        for j in range(len(key)):
            print(arr[i][j], end=" ", flush=True)
        print()

def cipher_decryption(encrypted, key):

    keyword_num_list = keyword_num_assign(key)
    num_of_rows = int(len(encrypted) / len(key))

    num_loc = get_number_location(key, keyword_num_list)

    # Converting message into a grid
    arr = [[0] * len(key) for i in range(num_of_rows)]

    # decipher
    plain_text = ""
    k = 0
    itr = 0

    for i in range(len(encrypted)):
        d = 0
        if k == len(key):
            k = 0
        else:
            d: int = int(num_loc[k])
        for j in range(num_of_rows):
            arr[j][d] = encrypted[itr]
            itr += 1
        if itr == len(encrypted):
            break
        k += 1

    print()

    for i in range(num_of_rows):
        for j in range(len(key)):
            plain_text += str(arr[i][j])
    return plain_text

plain_text = "Attack by sea and land at dawn!"
key = "fleet"

msg = plain_text.replace(" ","").upper()
msgkey = key.upper()

encrypted = cipher_encryption(msg, msgkey)
decrypted = cipher_decryption(encrypted, msgkey)

print ("Plain Text: " + plain_text)
print ("Encrypted Text: " + encrypted)
print ("Decrypted Text: " + decrypted)
print ()
print_grid(msg, key)

