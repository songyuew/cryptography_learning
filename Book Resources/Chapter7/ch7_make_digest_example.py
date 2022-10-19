import hashlib
import hmac

def make_digest(message):
    "Return a digest for the message."

    myKey = b'this_is_my_secret'
    hash = hmac.new(myKey, message, hashlib.sha3_256)
    return hash.hexdigest().encode('utf-8')

# You must encode your message before it is hashed.
message = b'This is a test of the emergency broadcast system; it is only a test.'
rd = make_digest(message)
print (rd)
