def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
    
def main():
    p = int(input("Input p: "))
    q = int(input("Input q: "))
    n = p*q
    phi = (p-1)*(q-1)
    e = int(input("Input e: "))
    d = modinv(e, phi)

    # decrypt the message
    c = int(input("Input c: "))
    m = pow(c, d, n) # calculate c^d mod n
    print("Decrypted message: " + str(m))

main()