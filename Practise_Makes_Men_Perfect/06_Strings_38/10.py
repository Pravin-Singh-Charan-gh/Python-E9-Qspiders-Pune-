# Exercise 10. Vowel Counter
# Practice Problem: Write a program to count the total number of vowels (a, e, i, o, u) in a given string.

txt = input('Enter the string : ')
ans = 0
for ch in txt:
    if ch in 'AEIOUaeiou':
        ans += 1
print('Vowel Count :',ans)