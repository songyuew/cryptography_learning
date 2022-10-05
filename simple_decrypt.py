from cryptography.fernet import Fernet
from getpass import getpass

# convert to byte string
key = getpass("Please input the key: ").encode()

f = Fernet(key)
cipher = input("Please input the cipher to decrypt: ").encode()
msg = f.decrypt(cipher)

print("-----------------MESSAGE START-----------------")
print(msg.decode())
print("------------------MESSAGE END------------------")