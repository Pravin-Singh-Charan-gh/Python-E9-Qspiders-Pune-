##6.	Check triangle type after validating sides.

a = int(input('Enter first triangle side : '))
b = int(input('Enter second triangle side : '))
c = int(input('Enter third triangle side : '))

if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print('Equilateral Triangle')
    elif a==b or b==c or a==c:
        print('Isoscales Triangle')
    else:
        print('Scalene Triangle')
else:
    print('Invalid Triangle')