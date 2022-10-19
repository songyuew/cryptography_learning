
# A school primality test method
def isPrime(n):
    # Corner case
    if n <= 1:
        return False

    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False;
    return True

print(isPrime(11))
print(isPrime(14))