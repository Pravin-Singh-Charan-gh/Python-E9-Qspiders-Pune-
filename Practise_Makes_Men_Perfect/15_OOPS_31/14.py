# Exercise 14: verride Parent Method Using super()
# Problem Statement: Write a Python program where a Vehicle parent class has a seating_capacity() method that accepts a capacity argument. Create a Bus child class that overrides this method to provide a default seating capacity of 50, using super() to call the parent’s version internally.

class Vehicle:
    def __init__(self,name,max_speed):
        self.name = name
        self.max_speed = max_speed

    def seating_capacity(self,capacity):
        print(f'{self.name} seating capacity is {capacity}')

class Bus(Vehicle):
    def seating_capacity(self):
        super().seating_capacity(50)

b1 = Bus('Cosmo',150)
b1.seating_capacity()