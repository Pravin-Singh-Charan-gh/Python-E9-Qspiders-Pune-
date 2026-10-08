# Exercise 5. Create an Inner Function
# Practice Problem: Create an outer function that accepts two parameters, a and b. Inside, create an inner function that calculates the addition of a and b. The outer function should then add 5 to that sum and return the final result.

def outer(a,b):
    def inner(a,b):
        return a+b
    return inner(a,b)+5

print(outer(2,2))