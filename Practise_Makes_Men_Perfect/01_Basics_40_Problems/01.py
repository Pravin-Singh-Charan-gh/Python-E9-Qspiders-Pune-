# Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.

def product_and_sum(a,b):
    product = a*b
    if product<=1000:
        return product
    else:
        return a+b

a = int(input('Enter first number : '))
b = int(input('Enter second number : '))

print(product_and_sum(a,b))