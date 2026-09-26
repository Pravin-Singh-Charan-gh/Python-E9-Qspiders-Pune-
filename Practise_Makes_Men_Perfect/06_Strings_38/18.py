# Exercise 18. Count all letters, digits, and special symbols from a given string
# Practice Problem: Write a program to count all letters, digits, and special symbols from a given string.

txt = input('Enter the string : ')

alpha = digits = special = 0

for ch in txt:
    if ch.isalpha():
        alpha += 1
    elif ch.isdigit():
        digits+=1
    else:
        special+=1
print('Letters :',alpha)
print('Digits :',digits)
print('Special Characters :',special)