# Exercise 14. Reverse an integer number
# Practice Problem: Write a program to reverse a given integer number (e.g., 76542 should become 24567).

n = int(input('Enter the number : '))

rev = 0
t = n

while t:
    rev = rev*10 + t%10
    t//=10

print(rev)