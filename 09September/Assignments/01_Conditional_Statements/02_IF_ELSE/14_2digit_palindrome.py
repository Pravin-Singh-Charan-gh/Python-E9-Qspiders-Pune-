##14.	Check if a number is two-digit and palindrome.

n = int(input('Enter a number : '))

if 10<=n<=99 and n%11==0:
    print('YES')
else:
    print('No')