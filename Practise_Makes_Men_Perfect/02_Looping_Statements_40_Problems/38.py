# Exercise 38. Find the sum of the series up to n terms
# Practice Problem: Write a program to calculate the sum of the series 2 + 22 + 222 + 2222 + …. up to N terms. For example, if n=5, the series is 2 + 22 + 222 + 2222 + 22222.

n = int(input('Enter the number : '))
num = 0
s= 0
for i in range(n):
    num = num*10 + 2
    s+=num
print(s)