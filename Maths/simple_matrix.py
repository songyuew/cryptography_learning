import numpy as npy

'''
solve the following equations:
a + b = 35
2a + 4b = 94
'''
A = npy.array([[1,1],[2,4]])
B = npy.array([[35],[94]])

# find the inverse of A
A_inv = npy.linalg.inv(A)
print(f"A inverse: {A_inv}")

# solve X
X = A_inv @ B
print(f"X: {X}")
