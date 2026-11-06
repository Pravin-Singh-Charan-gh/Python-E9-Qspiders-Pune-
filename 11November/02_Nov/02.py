from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self,name,brand,price):
        self.name = name
        self.brand = brand 
        self.price = price

    @abstractmethod
    def engine():
        pass

    @abstractmethod
    def no_of_wheels():
        pass 

class Car(Vehicle):
    def engine(self):
        self.engine = 'Turbo'

    def no_of_wheels(self):
        self.no_of_wheels = 4

class Bike(Vehicle):
    def engine(self):
        self.engine = 'Petrol Engine'

    def no_of_wheels(self):
        self.no_of_wheels = 2

thar = Car('Thar','Mahindra',1200000)
thar.engine()
thar.no_of_wheels()
print(thar.engine)
print(thar.no_of_wheels)

bullet = Bike('Classic 350','Royal Enfield',2500000)
bullet.engine()
bullet.no_of_wheels()
print(bullet.engine)
print(bullet.no_of_wheels)