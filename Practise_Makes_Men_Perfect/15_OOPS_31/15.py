# Exercise 15: Add Maintenance Fee in Child Class via super()
# Problem Statement: Write a Python program that creates a Vehicle parent class with a base fare, then extends a Taxi child class that adds a 10% maintenance fee on top of the base fare using super().

class Vehicle:
    def __init__(self,base_fare):
        self.base_fare = base_fare

class Taxi(Vehicle):
    def __init__(self,base_fare):
        super().__init__(base_fare)
        self.maintenance_fee = base_fare*10//100

    def total_fare(self):
        return self.base_fare + self.maintenance_fee

t1 = Taxi(100)
print(f'Base Fare : {t1.base_fare}')
print(f'Total Fare : {t1.total_fare()}')