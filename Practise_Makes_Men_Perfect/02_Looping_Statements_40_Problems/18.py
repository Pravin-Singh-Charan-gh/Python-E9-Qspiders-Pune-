# Exercise 18. Collatz Conjecture: Generate a sequence until it reaches 1
# Practice Problem: The Collatz conjecture states that if you start with any positive integer n, and if n is even, divide it by 2; if n is odd, multiply it by 3 and add 1. Repeat the process. The sequence will always eventually reach 1. Write a program to print this sequence for a given number.

n = int(input('Enter the number : '))

t = n
while t!=1:
    print(t)
    if not t%2: t//=2
    else:t= t*3+1

print(t)
