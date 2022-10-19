from cryptosteganography import CryptoSteganography

# open sound file
mediafile = 'chapter6/steg/file_example_MP3_700KB.mp3'
message = None

with open(mediafile, "rb") as f:
   message = f.read()

print()
print('The program is looking for an image named dogs.jpg\n')
origfile = "chapter6\steg\dogs.jpg"
print('The image with the hidden audio file will be called steg_audio_dogs.png\n')
modfile = "chapter6\steg\steg_audio_dogs.png"

key = "1111222233334444!"
crypto_steganography = CryptoSteganography(key)
crypto_steganography.hide(origfile, modfile, message)

print('The extracted data will be called decrypted_sample2.mp3 \n')
decrypted = 'decrypted_sample2.mp3'
secret_bin = crypto_steganography.retrieve(modfile)

# Save the data to a new file
with open(decrypted, 'wb') as f:
    f.write(secret_bin)

