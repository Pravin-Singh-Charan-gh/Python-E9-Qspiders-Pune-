#Write a program to find how many times the substring “Emma” appears in a given string.

def count_emma(txt):
    return txt.count('Emma')

txt = input('Enter the string : ')
print(count_emma(txt))
