#WAP to check if roots of quadratic equation are real, equal or imaginary
# b^2 - 4ac => if -ve->imaginary roots, if 0-> equal, +ve-> real roots


a = int(input("Enter coefficient of x^2: "))
b = int(input("Enter coefficient of x: "))
c = int(input("Enter constent : "))

m = (b**2) - 4*a*c

if m>0:
    print('real roots')
elif m==0:
    print('equal roots')
elif m<0:
    print('Imaginary roots')
