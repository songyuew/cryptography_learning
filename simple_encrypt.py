from cryptography.fernet import Fernet

key = Fernet.generate_key()
print("-------------------KEY START-------------------")
print(key.decode())
print("--------------------KEY END--------------------")

f = Fernet(key)
msg = input("Please input the message to encrypt: ")
tok = f.encrypt(msg.encode())
print("-----------------CIPHER START------------------")
print(tok.decode())
print("------------------CIPHER END-------------------")