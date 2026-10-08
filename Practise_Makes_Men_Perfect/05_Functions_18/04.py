# Exercise 4. Function with Default Argument
# Practice Problem: Create a function show_employee() that accepts an employee’s name and salary. If the salary is not provided in the function call, the function should automatically assign a default value of 9000.

def show_employee(ename,sal=1000):
    print('Name :',ename)
    print('Salary :',sal)

show_employee('Pravin',100000)