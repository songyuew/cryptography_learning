

import urllib.request, random, ssl
import operator
from itertools import cycle
from functools import reduce


def shiftBy(c, n):
    shift = chr(((ord(c) - ord('a') + n) % 26) + ord('a'))
    return shift

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
    readText = readText.decode('utf-8')
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

def decryptIndex(keys, ciphertext):
    """Decrypt the string and return the plaintext"""
    key = ""
    ALPHA = 'abcdefghijklmnopqrstuvwxyz'
    ciphertext = ciphertext.upper()
    ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(keys)):
        key = key + chr(keys[i] + 65)

    pairs = list(zip(ciphertext, cycle(key)))
    result = ''


    for pair in pairs:
        total = reduce(lambda x, y: ALPHA.index(x) - ALPHA.index(y), pair)
        result += ALPHA[total % 26]

    return result

def findKeyPos(message, keyLength, keyPos):
    frequency = {}
    allKeys = []
    return_key = 0
    tolerance = .01
    normal_freqs = {'a': 0.080642499002080981, 'c': 0.026892340312538593, 'b': 0.015373768624831691, 'e': 0.12886234260657689, 'd': 0.043286671390026357, 'g': 0.019625534749730816, 'f': 0.024484713711692099, 'i': 0.06905550211598431, 'h': 0.060987267963718068, 'k': 0.0062521823678781188, 'j': 0.0011176940633901926, 'm': 0.025009719347800208, 'l': 0.041016761327711163, 'o': 0.073783151266212627, 'n': 0.069849754102356679, 'q': 0.0010648594165322703, 'p': 0.017031440203182008, 's': 0.063817324270355996, 'r': 0.06156572691936394, 'u': 0.027856851020401599, 't': 0.090246649949305979, 'w': 0.021192261444145363, 'v': 0.010257964235274787, 'y': 0.01806326249861108, 'x': 0.0016941732664605912, 'z': 0.0009695838238376564}


    lowerMessage = message.lower()
    sampling = lowerMessage[keyPos::keyLength]

    for ascii in range(ord('a'), ord('a')+26):
        frequency[chr(ascii)] = float(sampling.count(chr(ascii)))/len(sampling)
        
    sum_freqs_squared = 0.0
    for ltr in frequency:
        sum_freqs_squared += frequency[ltr]*frequency[ltr]

    for possible_key in range(1, 26):
        sum_f_sqr = 0.0
        for ltr in normal_freqs:
            caesar_guess = shiftBy(ltr, possible_key)
            freqCalc = normal_freqs[ltr]*frequency[caesar_guess]
            sum_f_sqr += freqCalc
            
            engValue = abs(sum_f_sqr - .065)
            if engValue < tolerance:
                allKeys.append(possible_key)

    return allKeys

def getKey(encrypted, kl, dictionary):

    keys = []
    testKey = []
    defaultKey = []

    for i in range (0,kl):
        keyPos = findKeyPos(encrypted,16,i)
        answerLen =  len(keyPos)
        answerIndex = 0
        if answerLen > 1:
            defaultKey = keys[:]
            testKey = keys[:]
            defaultKey.append(keyPos[0])
            decrypted = decryptIndex(defaultKey,encrypted)
            defaultScore = getFitnessScore(decrypted, dictionary)
            for a in range(1,answerLen):
                testKey.append(keyPos[a])
                decrypted = decryptIndex(testKey,encrypted)
                testScore = getFitnessScore(decrypted, dictionary)
                if testScore > defaultScore:
                    answerIndex = a
                    defaultKey = testKey
                
        keys.append(keyPos[answerIndex])
        fullKey = ""
        for i in range(len(keys)):
            fullKey = fullKey + chr(keys[i] + 65)

    fullKey = ""
    for i in range(len(keys)):
        fullKey = fullKey + chr(keys[i] + 65)

    return (fullKey)


myDictionary = getDictionary()
cipherText = getEncryptedData()
freqScore = getLetterFreqs(cipherText)
fitScore = getFitnessScore(cipherText, myDictionary)
keyLength = getKeyLength(cipherText)
decryptKey = getKey(cipherText, keyLength, myDictionary)
    

print ()
print ("The frequency score for this file is: ", freqScore)
print ()
print ("The fitness score for this file is: ", fitScore)
print()
print ("The key length for this file is: ", keyLength)
print ()
print ("The decryption key for this file is: ", decryptKey)
print ()
