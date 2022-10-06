def toAtBash(text):
    characters = list(text.upper())
    result = ""
    for character in characters:
        if character in code_dictionary:
            result += code_dictionary.get(character)
        else:
            result += character # preserve non-alpha chars found
    return result

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
reverse_alphabet = list(reversed(alphabet))
code_dictionary = dict(zip(alphabet, reverse_alphabet))
plainText= "we hold these truths to be self-evident"
print(plainText)
cipherText = toAtBash(plainText)
print(cipherText)
cipherText = toAtBash(cipherText)
print(cipherText)

#we hold these truths to be self-evident
#DV SLOW GSVHV GIFGSH GL YV HVOU-VERWVMG
#WE HOLD THESE TRUTHS TO BE SELF-EVIDENT