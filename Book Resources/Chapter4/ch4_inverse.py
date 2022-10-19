a = 14
p = 101
a_inv = pow(a, p-2, p)
a_check = a * a_inv % p
print("The modular inverse is ", a_inv)
print("The check value should equal 1. It equals ", a_check)
