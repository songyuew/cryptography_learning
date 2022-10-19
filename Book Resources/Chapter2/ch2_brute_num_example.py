import random
# generate a password
generated_password = str(random.randint(0,9999))
# check values 0 - 9999
for i in range(10000):
    Trial = str(i)
    if Trial == generated_password:
        print('Found password: ' + generated_password)
