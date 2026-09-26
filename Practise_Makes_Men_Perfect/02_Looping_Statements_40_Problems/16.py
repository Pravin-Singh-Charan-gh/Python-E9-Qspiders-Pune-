# Exercise 16. Check if a number is a palindrome
# Practice Problem: Write a program to check if a given number is a palindrome. A palindrome number is a number that remains the same when its digits are reversed (e.g., 121, 343).

n = int(input('Enter the number : '))

rev = 0
t= n

while t:
    rev = rev*10 + t%10
    t//=10
if rev==n:
    print('Palindrome')
else:
    print('Not Palindrome')