##6.	Simple calculator (+, -, *, / based on user choice).

op1 = int(input('Enter the operand 1 : '))
operator = input('Enter the operation to perform (+,-,*,/) : ')
op2 = int(input('Enter the operand 2 : '))

if operator=='+':
    print(op1+op2)
elif operator=='-':
    print(op1-op2)
elif operator=='*':
    print(op1*op2)
elif operator=='/':
    print(op1/op2)
else:
    print('Invalid Operator')