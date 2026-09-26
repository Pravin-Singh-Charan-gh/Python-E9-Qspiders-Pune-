# Exercise 35. Perfect number check
# Practice Problem: Write a program to check if a number is a “Perfect Number.” A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding the number itself). For example, 6 is perfect because 1 + 2 + 3 = 6.

def is_perfect(n):
    sm = 0

    for i in range(1,n//2+1):
        if n%i==0:
            sm+=i
    return sm==n
n = int(input('Enter the number : '))

print(is_perfect(n))
# 4