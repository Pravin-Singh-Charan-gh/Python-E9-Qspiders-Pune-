##Exercise 4. Calculate the sum of all numbers from 1 to N
#Practice Problem: Write a program that accepts a number from the user and calculates the sum of all numbers from 1 up to that number.

def count_sum(n):
    s = 0
    for i in range(1,n+1):
        s+=i
    return s

n = int(input('Enter the number : '))

print(count_sum(n))
