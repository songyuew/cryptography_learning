
from cryptosteganography import CryptoSteganography

key = "1111222233334444!"
crypto_steganography = CryptoSteganography(key)

print()
print('The program is looking for an image named ch6_secret_image.png\n')
origfile = "chapter6\steg\ch6_secret_image.png"
print('The image with the hidden message will be called steg_ch6_secret_image.png\n')
modfile = "chapter6\steg\steg_ch6_secret_image.png"

secretMsg = ""
message1 = "Sympathy for the favorite nation, facilitating the illusion of an imaginary common "
message2 = "interest in cases where no real common interest exists, and infusing into one the "
message3 = "enmities of the other, betrays the former into a participation in the quarrels and "
message4 = "wars of the latter without adequate inducement or justification."
secretMsg = secretMsg.join([message1, message2, message3, message4])


crypto_steganography.hide(origfile, modfile, secretMsg)
secret = crypto_steganography.retrieve(modfile)
print("The secret that is hidden in the file is:\n")
print(secret)
print()


print('Now we will try the wronge secret.\n')
key = "AnotherKey"
crypto_steganography = CryptoSteganography(key)
secret = crypto_steganography.retrieve(modfile)
print('The secret message is: {} \n'.format(secret))
