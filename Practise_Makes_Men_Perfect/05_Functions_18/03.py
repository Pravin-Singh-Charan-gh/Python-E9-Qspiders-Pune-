# Exercise 3. Return Multiple Values from a Function
# Practice Problem: Write a function calculation() that accepts two variables and calculates both addition and subtraction. The function must return both results in a single return statement.

def calculation(a,b):
    return (a+b,a-b)

a = int(input('Enter first number : '))
b = int(input('Enter second number : '))

ans = calculation(a,b)

