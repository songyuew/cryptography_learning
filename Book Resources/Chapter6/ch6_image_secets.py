print('The program is looking for a file named: ch6_secret_image.jpg')
fo = open("Chapter6\ch6_secret_image.jpg", "rb")
image = fo.read()
fo.close()
print()
print("The secret key is 42.")
image = bytearray(image)
key = 42
for index, value in enumerate(image):
    image[index] = value^key

print()
print('The image has been encrypted. Review e_ch6_secret_image.jpg')

fo = open("Chapter6\e_ch6_secret_image.jpg", "wb")
fo.write(image)
fo.close()
image = bytearray(image)
for index, value in enumerate(image):
    image[index] = key^value

print()
print('The image has now been decrypted. Review d_ch6_secret_image.jpg')

fo = open("Chapter6\d_ch6_secret_image.jpg", "wb")
fo.write(image)
fo.close()
