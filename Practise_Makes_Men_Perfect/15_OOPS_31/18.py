# Exercise 18: Shape Subclasses with Custom area() Methods
# Problem Statement: Write a Python program that defines a Shape base class with an area() method, then implements it in Circle, Square, and Triangle subclasses using the appropriate geometric formulas.

import math
class Shape:
    def area(self):
        return 0
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return round(math.pi*self.radius*self.radius,2)

class Square(Shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side**2
    
class Triangle(Shape):
    def __init__(self,s1,s2,s3):
        self.s1 =s1
        self.s2 =s2
        self.s3 =s3

    def area(self):
        s = (self.s1 + self.s2 + self.s3)/3
        return math.sqrt(s*(s-self.s1)*(s-self.s2)*(s-self.s3))
    