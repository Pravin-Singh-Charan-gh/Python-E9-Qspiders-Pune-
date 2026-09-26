# Exercise 33. Word frequency counter

# Practice Problem: Write a program to count the frequency of each word in a given string.

text = "apple banana apple orange banana apple"

words = text.split()

freq = dict()

for word in words:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
print(freq)

# 3