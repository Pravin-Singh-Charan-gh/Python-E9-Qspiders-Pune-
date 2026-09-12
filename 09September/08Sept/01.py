#WAP to check whether the number is palindrome or not without typecasting

n = int(input('Enter a number : '))

temp = n
ans = 0

while temp:
    rem = temp%10
    ans = ans*10+rem
    temp//=10
if n==ans:
    print('Palindrome')
else:
    print('Not Palindrome')
print('===========CODE EXECUTED===========')
