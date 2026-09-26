# Exercise 14. N-th Character Removal
# Practice Problem: Write a program to remove the character at index i from a string.

txt = input('Enter the string : ')
index = int(input('Enter the index : '))

ans = txt[:index]+txt[index+1:]
print(ans)