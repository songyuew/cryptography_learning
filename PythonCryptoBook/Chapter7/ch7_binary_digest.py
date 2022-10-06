import base64
import hmac
import hashlib

myKey = b'this_is_my_secret'
with open('chapter7/test.txt', 'rb') as f:
    body = f.read(5)

hash = hmac.new(myKey, body, hashlib.sha256,)
digest = hash.digest()
print(base64.encodebytes(digest))
