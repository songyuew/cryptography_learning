def isPrime(x):
    x = abs(int(x))
    if x < 2:
        return "Less than 2", False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False
    else:
        for n in range(3, int(x ** 0.5) + 2, 2):
            if x % n == 0:
                return n, False
        return True

print(isPrime(100000007))
print(isPrime(1))