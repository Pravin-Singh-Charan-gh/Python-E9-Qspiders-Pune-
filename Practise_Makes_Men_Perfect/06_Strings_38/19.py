# Exercise 19. Create a mixed string using alternating characters
# Practice Problem: Given two strings, s1 and s2, create a third string made of the first char of s1, then the last char of s2, Next, the second char of s1 and the second-to-last char of s2, and so on. Any left-over chars go at the end of the result.

s1 = input('Enter first string : ')
s2 = input('Enter second string : ')

ans = ''
i = 0
j = 1
while i<len(s1) and j<=len(s2):
    ans = ans + s1[i]+s2[-j]
    i+=1
    j+=1
ans = ans + s1[i:]
ans = ans + s2[:-j:-1]

print(ans)