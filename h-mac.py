'''
The key acts as the salt, so rainbow attack will not work
The salt is actually a password, which is known to both party and remains confidential to others
'''

import hmac

msg = input("Please input the message: ").encode()
key = input("Please input the key: ").encode()
hDigest = hmac.new(key,msg,digestmod="MD5").hexdigest()
print(hDigest)