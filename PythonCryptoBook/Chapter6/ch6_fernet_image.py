from cryptography.fernet import Fernet
import os

def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()

def encrypt(filename, newfile, key):
    """
    Given a plain image (str), the new file name,  and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(newfile, "wb") as file:
        file.write(encrypted_data)

def decrypt(filename, newfile, key):
    """
    Given a encrypted file (str), the new file name, and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(newfile, "wb") as file:
        file.write(decrypted_data)

key = Fernet.generate_key()

enc = encrypt("chapter6\ch6_secret_image.jpg", "chapter6\e_ch6_secret_image.jpg", key)
dec = decrypt("chapter6\e_ch6_secret_image.jpg", "chapter6\d_ch6_secret_image.jpg", key)