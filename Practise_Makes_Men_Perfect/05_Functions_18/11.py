# Exercise 11. Create a Function with Keyword Arguments
# Practice Problem: Create a function print_info(**kwargs) that accepts an arbitrary number of keyword arguments and prints the key-value pairs.

def print_info(**kwargs):
    for key,value in kwargs.items():
        print(key,':',value)

print_info(name="Alice", age=30, city="New York")
