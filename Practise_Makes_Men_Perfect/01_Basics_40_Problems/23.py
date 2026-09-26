# Write a program to check if a given number is a palindrome. A palindrome number remains the same when its digits are reversed (e.g., 121, 545).

def is_palindrome(n):
    t = n
    rev = 0

    while t:
        rev = rev*10 + (t%10)
        t//=10
    return rev==n

n = int(input('Enter the number : '))
if is_palindrome(n):
    print('Palindrome')
else:
    print('Not Palindrome')