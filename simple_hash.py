import hashlib

plaintext_password = b"password"
hashed_sha512 = hashlib.sha512(plaintext_password).hexdigest()
print(hashed_sha512)