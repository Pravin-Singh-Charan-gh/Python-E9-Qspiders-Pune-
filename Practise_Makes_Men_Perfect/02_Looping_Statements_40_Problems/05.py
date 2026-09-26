##Exercise 4. Print multiplication table of a given number
##Practice Problem: Create a program that takes an integer and prints its multiplication table from 1 to 10.

def print_table(n):
    for i in range(1,11):
        print(f"{n}X{i} = {n*i}")

n = int(input('Enter the number : '))
print_table(n)
