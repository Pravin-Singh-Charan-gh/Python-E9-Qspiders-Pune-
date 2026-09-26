##Exercise 29. Word Length Analysis
##Practice Problem: Create a list of 5 words. Write a loop that iterates through the list and prints each word alongside its character count.

def word_length(words):
    for word in words:
        print(word,":",len(word))

words = eval(input('Enter the list of words : '))

word_length(words)
