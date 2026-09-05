#WAP to print fibonacci series up to N terms

n = int(input('Enter the number : '))

a = 0
b = 1

i=1

while i<=n:
    print(a, end=', ')
    a,b=b,b+a
    i+=1
