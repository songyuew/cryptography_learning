"""
This is used in the key generation of RSA

Input: a positive integer n
Function output: the count of numbers i in {1,2,3,...,n-1} that are relatively prime to n: gcd(i,n)=1

If n is prime, then the output of Euler Totient is n - 1 (because n have no factors except 1 and itself)
"""

# Euclidean Algorithm 
def gcd(a, b):
    if(a == 0):
        return b
    return gcd(b % a, a)

def EulerTotient(n):
    result = []
    for i in range(1,n):
        if(gcd(i,n) == 1):
            result.append(i)
    return result

def main():
    n = int(input())
    res = EulerTotient(n)
    print(res)
    print()
    print(f"Count: {len(res)}")

main()