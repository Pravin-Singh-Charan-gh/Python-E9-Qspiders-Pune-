# Exercise 5. Calculate the Product of All Elements
# Practice Problem: Multiply every number in a list together to find the total product.

l = eval(input('Enter the list : '))

product = 1
for i in l:
    product*=i
print('Product :',product)