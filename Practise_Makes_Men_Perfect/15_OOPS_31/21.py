##Exercise 21: Vehicle Class Hierarchy with Bike, Truck & Bus
##Problem Statement: Write a Python program that defines a Vehicle base class and creates Bike, Truck, and Bus subclasses, each defining a unique max_speed attribute and a describe() method.

class Vehicle:
    def __init__(self,max_speed):
        self.max_speed = max_speed
    def describe(self):
        print(f'{type(self).__name__}- Max-speed : {self.max_speed}')
    
class Bike(Vehicle):
    def __init__(self):
        super().__init__(120)
        
class Truck(Vehicle):
    def __init__(self):
        super().__init__(100)
        
class Bus(Vehicle):
    def __init__(self):
        super().__init__(110)

v1 = Vehicle(100)
b1 = Bike()
t1 = Truck()
bus1 = Bus()
v1.describe()
b1.describe()
t1.describe()
bus1.describe()
