
import math
def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            amount += 1
    return amount

for n in range(1,20) :
    print("Φ(",n,") = ",phi(n))