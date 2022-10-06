
import urllib.request, ssl

# URL to Common English Words
commonWordsPath = "https://raw.githubusercontent.com/noidentity29/AppliedCryptoPython/master/common_en_words.txt"

# create URL request
response = urllib.request.urlopen(commonWordsPath, context=ssl._create_unverified_context())
readText = response.read()

# the file is in a binary format, decode
fileOfWords = readText.decode('utf-8')

# create an array for each word
words = fileOfWords.split()

# print word list
for word in words:
    print (word)

# filter out the shorter words
longerwords = list(filter(lambda x: len(x)> 2, words))

# print out longer words
for word in longerwords:
    print (word)

