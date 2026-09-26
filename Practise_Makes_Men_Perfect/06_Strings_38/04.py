##Exercise 4. Create a new string made of the first, middle, and last characters of each input string
##Practice Problem: Given two strings, s1 and s2, create a new string from the first, middle, and last characters of each input string.

s1 = input('Enter the first string : ')
s2 = input('Enter the second string : ')

l1 = len(s1)
l2 = len(s2)

ans = s1[0]+s2[0]+s1[l1//2]+s2[l2//2]+s1[-1]+s2[-1]
print(ans)
