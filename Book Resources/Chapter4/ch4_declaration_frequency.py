import urllib.request, ssl

# get the text of the Declaration of Independence
response = urllib.request.urlopen("https://raw.githubusercontent.com/noidentity29/AppliedCryptoPython/master/declaration.txt", context=ssl._create_unverified_context())
originalText = response.read()

# Strip out all non-alhphabet characters
# There are a number of ways to do this but this is the simplest to understand
modifiedText = str(originalText.strip())
modifiedText = modifiedText.replace(" ", "")
modifiedText = " ".join(modifiedText.split())
modifiedText = modifiedText.lower()

plaintext = ""
for c in modifiedText:
    if (c.isalpha()):
        plaintext = plaintext + c


# Determine the frequency analysis of the plaintext
frequency = {}
for ascii in range(ord('a'), ord('a')+26):
    frequency[chr(ascii)] = float(plaintext.count(chr(ascii)))/len(plaintext)

sum_freqs_squared = 0.0
for ltr in frequency:
    sum_freqs_squared += frequency[ltr]*frequency[ltr]

# Results
print()
print ("The frequency should be near .065 if plaintext in English: " + str(sum_freqs_squared))

