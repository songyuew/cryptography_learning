

import urllib.request, random, ssl
import operator


def getLetterFreqs(text):
    frequency = {}
    for ascii in range(ord('a'), ord('a')+26):
        frequency[chr(ascii)] = float(text.count(chr(ascii)))/len(text)

    sum_freqs_squared = 0.0
    for ltr in frequency:
        sum_freqs_squared += frequency[ltr]*frequency[ltr]
    return sum_freqs_squared

def getTextOnly(text):
    # Strip out all non-alhphabet characters
    # There are a number of ways to do this but this is the simplest to understand
    modifiedText = str(text.strip())
    modifiedText = modifiedText.replace(" ", "")
    modifiedText = " ".join(modifiedText.split())
    modifiedText = modifiedText.lower()
    return modifiedText

def getEncryptedData():
    encryptedFilePath = "https://raw.githubusercontent.com/noidentity29/AppliedCryptoPython/master/encryptedmoby.txt"
    
    response = urllib.request.urlopen(encryptedFilePath, context=ssl._create_unverified_context())
    readText = response.read()
    textOnly = getTextOnly(readText)
    return textOnly

def getFitnessScore(message, longerwords):

    score = 0.0
    for word in longerwords:
        wordWeight = message.count(word)
        if wordWeight>0:
            score += wordWeight * 50 * len(word)
    return score

def getDictionary():
    
    commonWordsPath = "https://raw.githubusercontent.com/noidentity29/AppliedCryptoPython/master/common_en_words.txt"
    ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    
    # create URL request
    response = urllib.request.urlopen(commonWordsPath, context=ssl._create_unverified_context())
    readText = response.read()

    # the file is in a binary format, decode
    fileOfWords = readText.decode('utf-8')

    # create an array for each word
    words = fileOfWords.split()

    # filter out the shorter words
    longerwords = list(filter(lambda x: len(x)> 2, words))

    return longerwords

def getKeyLength(encryptedText):
    highest = 0;
    highCtr = 0;
    encryptedText = encryptedText.lower()
    for KeyLength in range(1,26):
        sampling = encryptedText[::KeyLength]
        freqCheck =  getFreqs(sampling)
        if highest < freqCheck:
            highest = freqCheck
            highCtr = KeyLength

    return highCtr

def getFreqs(text):
    frequency = {}
    for ascii in range(ord('a'), ord('a')+26):
        frequency[chr(ascii)] = float(text.count(chr(ascii)))/len(text)

    sum_freqs_squared = 0.0
    for ltr in frequency:
        sum_freqs_squared += frequency[ltr]*frequency[ltr]
    return sum_freqs_squared

myDictionary = getDictionary()
cipherText = getEncryptedData()
freqScore = getLetterFreqs(cipherText)
fitScore = getFitnessScore(cipherText, myDictionary)
keyLength = getKeyLength(cipherText)

print ()
print ("The frequency score for this file is: ", freqScore)
print ()
print ("The fitness score for this file is: ", fitScore)
print()
print ("The key length for this file is: ", keyLength)
print ()
