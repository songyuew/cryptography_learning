# Note: this will only generate pseudoprime (there might be false positive)

"""
Fermat's little theorem:
p - prime number
a - any integer

for every a, 1 < a < p - 1,
a ^ (p - 1) % p = 1
"""

def checkPrime(x):
    # pow(a,b,c) = (a ^ b) % c 
    return pow(2, x-1, x) == 1

print(checkPrime(19))
print(checkPrime(31))
print(checkPrime(589))
print(checkPrime(5893529831))