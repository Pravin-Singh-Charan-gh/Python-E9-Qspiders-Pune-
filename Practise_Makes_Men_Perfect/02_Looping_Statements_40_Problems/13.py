# Exercise 13. Count total number of digits in a number
# Practice Problem: Write a program to count the total number of digits in a given integer using a while loop.

n = int(input('Enter the number : '))

count = 0
t = n
while t:
    count+=1
    t//=10
print(count)