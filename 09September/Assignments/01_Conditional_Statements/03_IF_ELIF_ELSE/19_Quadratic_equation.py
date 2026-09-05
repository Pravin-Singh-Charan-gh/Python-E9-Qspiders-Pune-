# 	Check if quadratic equation has real, equal, or imaginary roots.

a = int(input('Enter coefficient of x^2 : '))
b = int(input('Enter coefficient of x : '))
c = int(input('Enter constant : '))

m = b**2-(4*a*c)

if m>0:
    print('Real Roots')
elif m==0:
    print('Equal Roots')
elif m<0:
    print('Negative roots')