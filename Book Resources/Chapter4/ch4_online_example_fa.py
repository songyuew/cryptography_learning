
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
    
def getFitnessScore(message):
    lower = message.lower()
    score = 0.0
    for word in longerwords:
        wordWeight = lower.count(word)
        if wordWeight>0:
            score += wordWeight * 50 * len(word)
    return score

def getFreqKey(text):
    frequency = {}
    message = text.lower()
    normal_freqs = {'a': 0.080642499002080981, 'c': 0.026892340312538593, 'b': 0.015373768624831691, 'e': 0.12886234260657689, 'd': 0.043286671390026357, 'g': 0.019625534749730816, 'f': 0.024484713711692099, 'i': 0.06905550211598431, 'h': 0.060987267963718068, 'k': 0.0062521823678781188, 'j': 0.0011176940633901926, 'm': 0.025009719347800208, 'l': 0.041016761327711163, 'o': 0.073783151266212627, 'n': 0.069849754102356679, 'q': 0.0010648594165322703, 'p': 0.017031440203182008, 's': 0.063817324270355996, 'r': 0.06156572691936394, 'u': 0.027856851020401599, 't': 0.090246649949305979, 'w': 0.021192261444145363, 'v': 0.010257964235274787, 'y': 0.01806326249861108, 'x': 0.0016941732664605912, 'z': 0.0009695838238376564}
    tolerance = .013 
    for ascii in range(ord('a'), ord('a')+26):
        frequency[chr(ascii)] =  message.count(chr(ascii))    
    sorted_x = sorted(frequency.items(), key=operator.itemgetter(1), reverse=True)
    print (sorted_x)
    sortedkey = ""
    for i in range(0, len(sorted_x)):
        sortedkey += sorted_x[i][0]
    return sortedkey

def getTextOnly(text):
    # Strip out all non-alhphabet characters
    # There are a number of ways to do this but this is the simplest to understand
    modifiedText = str(text.strip())
    modifiedText = modifiedText.replace(" ", "")
    modifiedText = " ".join(modifiedText.split())
    modifiedText = modifiedText.lower()
    return modifiedText


encryptedFilePath = "https://raw.githubusercontent.com/noidentity29/AppliedCryptoPython/master//ch4_encrypted.txt"
commonWordsPath = "https://raw.githubusercontent.com/noidentity29/AppliedCryptoPython/master/common_en_words.txt"
ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

response = urllib.request.urlopen(encryptedFilePath, context=ssl._create_unverified_context())
readText = response.read()
cipherText = getTextOnly(readText)

# create URL request
response = urllib.request.urlopen(commonWordsPath, context=ssl._create_unverified_context())
readText = response.read()

# the file is in a binary format, decode
fileOfWords = readText.decode('utf-8')

# create an array for each word
words = fileOfWords.split()

# filter out the shorter words
longerwords = list(filter(lambda x: len(x)> 2, words))


keys = []
frequency = {}
frequency = getLetterFreqs(cipherText)

print ("Frequency of the cipherText: ", frequency)
print ()

keys = getFreqKey(cipherText)
print ()
print ("Frequency key: ", keys)
print ()

