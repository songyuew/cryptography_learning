import zlib
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from pathlib import Path

# Generate new key pair function
def generate_new_key_pair():
    # Generate a public/ private key pair using 4096 bits key length (512 bytes)
    new_key = RSA.generate(4096, e=65537)

    # The private key in PEM format
    private_key = new_key.exportKey("PEM")

    # The public key in PEM Format
    public_key = new_key.publickey().exportKey("PEM")

    private_key_path = Path('private.pem')
    private_key_path.touch(mode=0o600)
    private_key_path.write_bytes(private_key)

    public_key_path = Path('public.pem')
    public_key_path.touch(mode=0o664)
    public_key_path.write_bytes(public_key)


# RSA Encryption Function
def encrypt_blob(blob, public_key):
    #Import the Public Key and use for encryption using PKCS1_OAEP
    rsa_key = RSA.importKey(public_key)
    rsa_key = PKCS1_OAEP.new(rsa_key)

    #compress the data first
    blob = zlib.compress(blob)
    #In determining the chunk size, determine the private key length used in bytes
    #and subtract 42 bytes (when using PKCS1_OAEP). The data will be in encrypted
    #in chunks
    chunk_size = 470
    offset = 0
    end_loop = False
    encrypted = bytearray()

    while not end_loop:
        #The chunk
        chunk = blob[offset:offset + chunk_size]

        #If the data chunk is less then the chunk size, then we need to add
        #padding with " ". This indicates the we reached the end of the file
        #so we end loop here
        if len(chunk) % chunk_size != 0:
            end_loop = True
            #chunk += b" " * (chunk_size - len(chunk))
            chunk += bytes(chunk_size - len(chunk))
        #Append the encrypted chunk to the overall encrypted file
        encrypted += rsa_key.encrypt(chunk)

        #Increase the offset by chunk size
        offset += chunk_size

    #Base 64 encode the encrypted file
    return base64.b64encode(encrypted)

# RSA Decryption Function
def decrypt_blob(encrypted_blob, private_key):

    # Import the Private Key and use for decryption using PKCS1_OAEP
    rsakey = RSA.importKey(private_key)
    rsakey = PKCS1_OAEP.new(rsakey)

    # Base 64 decode the data
    encrypted_blob = base64.b64decode(encrypted_blob)

    # In determining the chunk size, determine the private key length used in bytes.
    # The data will be in decrypted in chunks
    chunk_size = 512
    offset = 0
    decrypted = bytearray()

    # keep loop going as long as we have chunks to decrypt
    while offset < len(encrypted_blob):
        # The chunk
        chunk = encrypted_blob[offset: offset + chunk_size]

        # Append the decrypted chunk to the overall decrypted file
        decrypted += rsakey.decrypt(chunk)

        # Increase the offset by chunk size
        offset += chunk_size

    # return the decompressed decrypted data
    return zlib.decompress(decrypted)


# generate_new_key_pair() # run if you don't already have a key pair

print("This program is looking for an image named 'cloud.jpg' in the chapter8 folder.")

private_key = open('private_key.pem').read()

print("The private key has been read.")

public_key = open('public_key.pem').read()

print("The public key has been read.")

unencrypted_file = Path('chapter8/cloud.jpg')
encrypted_file = unencrypted_file.with_suffix('.dat')
encrypted_blob = encrypt_blob(unencrypted_file.read_bytes(), public_key)

print("The cloud has been encrypted.")

# Write the encrypted contents to a file
fd = open("chapter8/e_cloud.jpg", "wb")
fd.write(encrypted_blob)
fd.close()

print("The encrypted image is named e_cloud.jpg")

# Our candidate file to be decrypted
fd = open("chapter8/e_cloud.jpg", "r")
encrypted_blob = fd.read()
fd.close()

print()
print("The contents of the encrypted file is too long to print.")
print()

# Write the decrypted contents to a file
fd = open("chapter8/d_cloud.jpg", "wb")
fd.write(decrypt_blob(encrypted_blob, private_key))
fd.close()

# Decrypt the encrypted blob
decrypt_blob(encrypted_blob, private_key)

print("The cloud has been decrypted. Examine the d_cloud.jpg file.")

