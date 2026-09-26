# Exercise 13: Bus Subclass Inheriting from Vehicle
# Problem Statement: Write a Python program to create a Vehicle parent class with name and max_speed attributes and a display() method. Then create a Bus child class that inherits everything from Vehicle without adding anything new, and confirm that an instance of Bus can access the parent’s method.

class Vehicle:
    def __init__(self,name,max_speed):
        self.name = name
        self.max_speed = max_speed

    def display(self):
        print(f'Name : {self.name}')
        print(f'Max Speed : {self.max_speed}')

class Bus(Vehicle):
    pass

b1 = Bus('Cosmo',150)
b1.display()