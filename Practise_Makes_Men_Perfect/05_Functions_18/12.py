# Exercise 12. Modifying Global Variables
# Practice Problem: Define a global variable global_var = 10. Write a function that successfully changes the value of this global variable to 20.

global_var=10

def fun():
    global global_var
    global_var=20

fun()
print(global_var)