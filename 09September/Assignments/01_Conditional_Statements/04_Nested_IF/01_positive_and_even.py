##1.	Check if number is positive AND even.

n = int(input('Enter a number : '))

if n>=0:
    print('Number is positive')
    if not n%2:
        print('Number is even')
else:
    print('Number is negative')