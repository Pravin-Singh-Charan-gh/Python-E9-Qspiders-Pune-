# Exercise 7. Assign a Different Name to Function and Call It
# Practice Problem: Assign a different name to the function display_student(name, age) and call it using the new name. For example, assign it to a variable called show_student.

def display_student(name,age):
    print(name,age)

show_student = display_student

show_student('Pravin',23)