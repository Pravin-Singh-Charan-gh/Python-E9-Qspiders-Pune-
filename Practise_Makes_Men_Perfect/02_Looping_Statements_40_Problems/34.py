# Exercise 34. Display fibonacci series up to 10 terms
# Practice Problem: Write a program to display the Fibonacci sequence up to 10 terms. The sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones.

a,b = 0,1
print(a)

for i in range(2,11):
    print(b)
    a,b=b,a+b
# 2