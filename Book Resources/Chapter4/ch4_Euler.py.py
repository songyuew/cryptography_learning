import math
import numpy as np
from matplotlib import pyplot as plt
def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            amount += 1
    return amount

for i in range (500):
    phi_n = phi(i)
    #print (i ,phi_n)
    plt . plot (i ,phi_n , 'o ')
    
plt.xlabel("Value of x")
plt.ylabel("Value of y")
plt.title("Euler's Theorem")
plt.show()
