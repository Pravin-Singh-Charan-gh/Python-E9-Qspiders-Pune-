##Exercise 2: Vehicle Class with Instance Attributes
##Problem Statement: Write a Python program to create a Vehicle class with two instance attributes: max_speed and mileage. Create an object of the class and print both attributes.

class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

v1 = Vehicle('Virtus',200,18)
print('Name :',v1.name)
print('Speed :',v1.max_speed)
print('Mileage :',v1.mileage)
