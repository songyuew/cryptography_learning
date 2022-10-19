import hashlib
def saltPassword_sha512(password):
    salt = b'cHp3'
    hashed = hashlib.sha512(salt + password).hexdigest()
    print ("%s:%s" % (salt, hashed)) # Store these
    return hashed

plaintext_password = b'Password'
hashed_sha512 = saltPassword_sha512 (plaintext_password)
