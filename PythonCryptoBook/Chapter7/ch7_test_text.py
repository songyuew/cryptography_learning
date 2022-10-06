import hmac
myKey = b'this_is_my_secret'
digest_maker = hmac.new(myKey)

with open('chapter7/test.txt', 'rb') as f:
    while True:
        block = f.read(1024)
        if not block:
            break

digest_maker.update(block)
digest = digest_maker.hexdigest()
print (digest)
