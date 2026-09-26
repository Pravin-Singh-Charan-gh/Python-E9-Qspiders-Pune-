# Exercise 17. Find factorial of a number
# Practice Problem: Write a program to use a loop to find the factorial of a given number (e.g., 5!). The factorial of N is the product of all integers from 1 to N.


n = int(input('Enter the number : '))

fact = 1
t= n

while t:
    fact*=t
    t-=1
print(fact)

