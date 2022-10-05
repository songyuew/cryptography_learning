n = int(input("Please input a six-digit number: "))
amt = int(input("Amount of random numbers to generate: "))

# keep squaring the number and get the digits in the middle as outcome
for i in range(amt):
    n = int(str(n ** 2).zfill(12)[3:9])
    print(n)
