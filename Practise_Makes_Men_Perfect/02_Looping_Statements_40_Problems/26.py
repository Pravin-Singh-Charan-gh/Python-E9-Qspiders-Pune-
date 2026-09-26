# Exercise 26. Print full multiplication table (1 to 10)
# Practice Problem: Write a program to print the full multiplication table from 1 to 10 in a grid format.

for i in range(1,11):
    for j in range(1,11):
        print(i*j,end=' ')
    print()