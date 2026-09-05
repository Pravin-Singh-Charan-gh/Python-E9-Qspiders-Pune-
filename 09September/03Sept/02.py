#WAP to check if 3 sides can make a triangle or not. if they can make check whether the triangle is equalateral, scalene or isosclese.

a = int(input('Enter first side of triangle : '))
b = int(input('Enter second side of triangle : '))
c = int(input('Enter third side of triangle : '))

if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print('Equaleral')
    elif a==b or b==c or a==c:
        print('Isosceles')
    else:
        print('Scalene')
 else:
     print('Invaid sides')
