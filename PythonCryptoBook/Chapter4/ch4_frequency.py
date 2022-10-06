
# initializing string 
test_str = "We hold these truths to be self-evident, that all men are created equal, "
test_str += "that they are endowed by their Creator with certain unalienable Rights, "
test_str += "that among these are Life, "
test_str += "Liberty and the pursuit of Happiness."

# get count of each element in string 
all_freq = {} 

for i in test_str: 
    if i in all_freq: 
        all_freq[i] += 1
    else: 
        all_freq[i] = 1

# printing result 
print()
print ("Count of all characters in the provided text is :\n " + str(all_freq)) 

# frequency using collections.Counter() 
from collections import Counter 

# initializing string 
test_str = "We hold these truths to be self-evident, that all men are created equal, "
test_str += "that they are endowed by their Creator with certain unalienable Rights, "
test_str += "that among these are Life, "
test_str += "Liberty and the pursuit of Happiness."

# using collections.Counter() to get 
# count of each element in string 
res = Counter(test_str) 

# printing result 
print()
print ("Count of all characters in the provided text is :\n " + str(res)) 
print()
