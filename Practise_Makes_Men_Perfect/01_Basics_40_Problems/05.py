#Write a program to swap the values of two variables, a and b, without using a third temporary variable.

a = int(input('Enter a : '))
b = int(input('Enter b : '))

print(f'Before Swap, a : {a}, b : {b}')
a,b=b,a
print(f'After Swap, a : {a}, b : {b}')

print('======================')
print('Again swaping without using tuple unpacking')
print(f'Before Swap, a : {a}, b : {b}')

a = a+b
b = a - b
a = a - b
print(f'After Swap, a : {a}, b : {b}')
