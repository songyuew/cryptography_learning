import hashlib
BLOCKSIZE = 65536
hasher = hashlib.sha256()

with open('chapter7/hmactestvectors.zip', 'rb') as afile:
    buf = afile.read(65536)

    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)

print(hasher.hexdigest())
