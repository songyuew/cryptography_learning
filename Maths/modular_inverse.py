print("Find the modular inverse of a, where a is an integer and the modulus, p is a prime.")
a = int(input("a: "))
p = int(input("p: "))

"""
a' (the modulus inverse of a) is n
(n * a) % p = 1 (definition) 
(a ^ (p - 1)) % p = 1 (Fermat's little theorem)
it can be concluded that n = (a ^ (p - 2)) % p
"""
a_inv = pow(a, p - 2, p)
print(f"The modular inverse of a is {a_inv}")
a_check = a * a_inv % p
print(f"Check: a * a_inv % p = {a_check}")
