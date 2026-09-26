# Exercise 17. Lowercase First
# Practice Problem: Write a program to arrange string characters such that all lowercase letters come first, followed by all uppercase letters.

txt = input('Enter the string : ')
ans = ('').join([ch for ch in txt if 'a'<=ch<='z']) + ('').join([ch for ch in txt if 'A'<=ch<='Z'])

print(ans)