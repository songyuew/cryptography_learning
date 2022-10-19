import hmac
from hashlib import md5

key = b'DECLARATION'
h = hmac.new(key,b'',md5)

# add content
h.update(b'We hold these truths to be self-evident, that all men are created equal')

# print the HMAC digest
print (h.hexdigest())
