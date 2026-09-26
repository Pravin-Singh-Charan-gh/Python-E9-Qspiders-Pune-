##Exercise 40. Introduction to Classes (OOP)
##Practice Problem: Create a Car class with attributes for make, model, and year. Include a method called start_engine() that prints a formatted string describing the car starting up.

class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def start_engine(self):
        print(f"{self.make} {self.model} {self.year} is starting up!.")

c1 = Car('Toyota','Fortuner','2016')
c1.start_engine()
