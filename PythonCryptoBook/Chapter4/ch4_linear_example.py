
import numpy as np

# solve the following linear equation
print ('1a + 1b = 35')
print ('2a + 4b = 94')

A = np.matrix([[1,1],[2,4]])
B = np.matrix([[35],[94]])

# find teh inverse of A
A_inverse = np.linalg.inv(A)
print (A_inverse)

# solve for X
X = A_inverse * B
print (X)

print('\n' * 3)
print('Next example:')
print('\n' * 3)

# solve the following linear equation
print ('1a + 1b = 35')
print ('2a + 4b = 94')

# create equations
a = np.array([[1, 1],[2,4]])
b = np.array([35, 94])

# print answers
print (np.linalg.solve(a, b))

