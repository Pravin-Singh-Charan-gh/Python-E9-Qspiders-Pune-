# Write a program to check if a given number is a palindrome (reads the same forwards and backwards).

def is_palindrome(n):
    rev = 0
    t = n
    while t:
        rem = t%10
        rev = rev*10 + rem
        t//=10
    return n==rev

n=int(input('Enter the number : '))
if is_palindrome(n):
            print('Palindrome')
else:
    print('No')


