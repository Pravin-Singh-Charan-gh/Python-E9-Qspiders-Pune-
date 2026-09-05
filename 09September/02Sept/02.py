n = int(input('Enter a number : '))

if n>0:
    if n%2:
        print('ODD')
    else:
        print('EVEN')
elif n==0:
    print('ZERO')
else:
    print('NEGATIVE')
