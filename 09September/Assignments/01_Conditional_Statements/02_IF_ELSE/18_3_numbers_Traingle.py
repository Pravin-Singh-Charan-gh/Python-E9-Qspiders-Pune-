##18.	Check if three numbers can form a triangle.

a = int(input('Enter the first side of triangle : '))
b = int(input('Enter the second side of triangle : '))
c = int(input('Enter the third side of triangle : '))

if a+b>c and a+c>b and b+c>a:
    print('Yes')
else:
    print('No')