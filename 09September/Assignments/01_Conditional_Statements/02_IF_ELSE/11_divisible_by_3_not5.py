##11.	Check if a number is divisible by 3 but NOT divisible by 5.

n = int(input('Enter a number : '))

if n%3==0 and n%5:
    print('YES')
else:
    print('NO')