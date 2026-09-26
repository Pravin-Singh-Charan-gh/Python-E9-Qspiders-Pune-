# Exercise 3: Frequency Map with Counter
# Practice Problem: Create a function that takes a string and returns a count of how many times each character appears. Ignore spaces and make it case-insensitive.

from collections import Counter

def char_count(txt):
    temp = txt.lower().replace(' ','')

    return Counter(temp)

txt = input('Enter the string : ')
print(char_count(txt))