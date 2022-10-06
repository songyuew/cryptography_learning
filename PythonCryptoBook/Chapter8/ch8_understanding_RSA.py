import random

#Euclid's algorithm - Chapter 4
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#Euclid's extended algorithm - Chapter 4
def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        return d + phi

# Verify the number is Prime - Chapter 4
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    #n = pq
    n = p * q

    #Phi is the totient of n
    phi = (p-1) * (q-1)

    #Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    #Use Euclid's Algorithm to verify copprimes for e and phi(n)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    #Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    
    #Return public and private keypair
    #Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    #Return the array of bytes
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    #Return the array of bytes as a string
    return ''.join(plain)
    

if __name__ == '__main__':

    print ("Chapter 8 - Understanding RSA\n")
    # First 20 prime numbers include:
    # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71
    p = int(input("Enter a prime number: "))
    q = int(input("Enter a second distinct prime number:"))
    print ("\nGenerating your public/private keypairs . . .")
    public, private = generate_keypair(p, q)
    print ("\nYour public key is {} and your private key is {}\n".format(public, private))
    message = input("Enter a message to encrypt with your public key: ")
    encrypted_msg = encrypt(public, message)
    print ("Your encrypted message is: {}".format(''.join(map(lambda x: str(x), encrypted_msg))))
    print ("\nDecrypting message with your personal private key ", private ," . . .")
    print ("\nYour message is: {}\n\n".format(decrypt(private, encrypted_msg)))

