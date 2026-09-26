# 14.	Find second largest among three numbers.

a = int(input('Enter first number : '))
b = int(input('Enter second number : '))
c = int(input('Enter third number : '))

if a>b>c or a<b<c:
    print(f'Second number is second largest : {b}')
elif b>a>c or b<a<c:
    print(f'First number is second largest : {a}')
else:
    print(f'Third number is second largest : {c}')

