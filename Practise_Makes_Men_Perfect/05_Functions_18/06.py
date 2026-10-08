# Exercise 6. Create a Recursive Function
# Practice Problem: Write a recursive function addition() that calculates the sum of numbers from 0 to 10. A recursive function is a function that calls itself to solve smaller instances of the same problem.

def addition(n):
    if not n:
        return 0
    return n+addition(n-1)

print(addition(10))