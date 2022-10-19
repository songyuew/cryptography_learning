import bcrypt

passwd = b"s$cret12"
salt = bcrypt.gensalt()
print(salt)
hashed = bcrypt.hashpw(passwd,salt)

# Password is stored with salt, each user will have a different salt. 
# Even if the hacker get both hash and salt plaintexts, he need to compute the separate rainbow table for each user.
print(hashed)