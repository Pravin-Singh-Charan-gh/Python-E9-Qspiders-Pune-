##Exercise 24: Vector Addition Using add Overloading
##Problem Statement: Write a Python program that creates a Vector class representing a 2D vector, and implements the __add__ dunder method so that two Vector objects can be added using the + operator.

class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,v):
        return Vector(self.x+v.x, self.y+v.y)

    def __repr__(self):
        return f'Vector({self.x},{self.y})'

v1 = Vector(2,3)
v2 = Vector(4,5)
ans = v1+v2
print(ans)
