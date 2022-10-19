import hashlib
hasher = hashlib.md5()
# from http://csrc.nist.gov/groups/STM/cavp/documents/mac/hmactestvectors.zip

with open('chapter7/hmactestvectors.zip', 'rb') as afile:
    buf = afile.read()
    hasher.update(buf)

print(hasher.hexdigest())
