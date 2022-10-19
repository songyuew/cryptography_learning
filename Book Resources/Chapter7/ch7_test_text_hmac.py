import hmac
import hashlib
myKey = b'this_is_my_secret'
digest_maker = hmac.new(myKey, b'', hashlib.sha256,)
with open("chapter7/test.txt", "wb") as hello_file:
    hello_file.write(b'Hello')
    hello_file.close()

# the test.txt file contains the bytes 'Hello'
with open('chapter7/test.txt', 'rb') as f:
    while True:
        block = f.read(5)
        if not block:
            break

digest_maker.update(block)
digest = digest_maker.hexdigest()
print(digest)

#6833cebacb9495c1cccba617d4b5f3aefda3dc03fcb3f8d070d61a09a4084a02
