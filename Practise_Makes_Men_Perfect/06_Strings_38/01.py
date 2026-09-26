##Exercise 1. Create a string made of the first, middle, and last character
##Practice Problem: Write a program to create a new string made of an input string’s first, middle, and last characters.

txt = input('Enter the string : ')

txt2 = txt[0]+txt[len(txt)//2]+txt[-1]

print(txt2)
