import math

def calculateProb(d, n):
  exponent = (-n * (n - 1)) / (2 * d)
  return 1 - math.e ** exponent;
  
# calculate the probability that at least 2 people share the same birthday, given there is a total of 23 people
print(calculateProb(365, 23)) 

#calculate the probability that there is a collision if the hash has 8 hex characters, and there are 1000 hashing operations
print(calculateProb(16**8, 1000)) 

