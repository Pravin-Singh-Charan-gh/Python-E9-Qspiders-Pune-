##Exercise 22: Identify Object’s Class Using type()
##Problem Statement: Write a Python program that creates objects from multiple classes and uses the built-in type() function to identify which class each object belongs to.

class Vehicle:
    pass
class Animal:
    pass
class Book:
    pass

v1 = Vehicle()
a1 = Animal()
b1 = Book()

print('Type of v1 : ',type(v1).__name__)
print('Type of a1 : ',type(a1).__name__)
print('Type of b1 : ',type(b1).__name__)
