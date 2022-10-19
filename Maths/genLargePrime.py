from secrets import randbits
from MillerRabin import isPrime

# number of iterations (different random a tried) for Miller-Rabin primality test
# high accuracy is required for crptography use!
k = 128

def genPrimeCandidate(length):
    p = randbits(length)

    """
    make sure the MSB and LSB of p is 1 (p is greater than 2 ^ (length - 1) and p is an odd number)
    | is the bitwise OR operator
    """
    p |= (1 << length - 1) | 1
    return p

def genPrimeNumber(length=2048):
    p = 4
    while not isPrime(p,k):
        p = genPrimeCandidate(length)
    return p

def main():
    print("Large prime p: ")
    p = genPrimeNumber()
    print(p)
    print()
    print("Large prime q: ")
    q = genPrimeNumber()
    print(q)
    print()
    print("Product of p and q: ")
    print(p * q)
    print("\n" * 3)

if __name__ == "__main__":
    main()