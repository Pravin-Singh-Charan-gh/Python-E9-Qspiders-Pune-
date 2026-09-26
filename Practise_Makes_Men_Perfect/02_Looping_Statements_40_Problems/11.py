# Exercise 11. Reverse a string using a for loop (no slicing)
# Practice Problem: Write a program that takes a string and reverses it using a for loop. While Python’s [::-1] shortcut is famous, reversing a string manually is a classic way to understand how sequences are constructed.

s = 'Python'
ans = ''
for ch in s:
    ans = ch+ans
print(ans)