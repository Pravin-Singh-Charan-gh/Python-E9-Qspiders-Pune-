##11.	Reverse number and check palindrome.

n = int(input('Enter the number : '))

rev = 0

t = n
while t:
    rem = t%10
    rev = rev*10 + rem
    t//=10

if rev == n:
    print('Palindrome')
else:
    print('Not palindrome')