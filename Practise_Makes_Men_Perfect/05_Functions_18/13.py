# Exercise 13. Recursive Factorial (Non-Negative Integers)
# Practice Problem: Write a recursive function to calculate the factorial of a non-negative integer.

def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)

print(fact(5))