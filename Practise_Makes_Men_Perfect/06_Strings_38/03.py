##Exercise 3. Append new string in the middle of a given string
##Practice Problem: Given two strings, s1 and s2, create a new string by appending s2 in the middle of s1.

s1 = input('Enter the first string : ')
s2 = input('Enter the second string : ')

l1 = len(s1)
ans = s1[:l1//2] + s2 + s1[l1//2:]
print(ans)
