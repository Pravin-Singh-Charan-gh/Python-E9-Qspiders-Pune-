# Exercise 2. Variable Length of Arguments (*args)
# Practice Problem: Create a function func1() such that it can accept a variable number of arguments and print all of them. Whether you pass two numbers or five, the function should handle them all without error.

def func1(*args):
    for i in args:
        print(i)

func1(input(),input(),input())