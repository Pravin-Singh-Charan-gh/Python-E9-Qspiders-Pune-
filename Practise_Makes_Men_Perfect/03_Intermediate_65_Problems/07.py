# Exercise 7: Palindrome Sentence
# Practice Problem: Write a function to check if a full sentence is a palindrome. You must ignore case, spaces, and all punctuation marks.

def is_palindrome(txt):
    clear_txt = [ch for ch in txt if ch.isalnum()]
    print(type(clear_txt))
    return clear_txt == clear_txt[::-1]

txt = input('Enter the text : ')
if is_palindrome(txt):
    print('Yes')
else:
    print('No')
