class Vehicle:
    def __init__(self,name,brand,color):
        self.name = name
        self.brand = brand 
        self.color = color 

    engine_type = 'Turbo'
    fuel = 'petrol'

class Car(Vehicle):
    no_of_wheels = 4

c1 = Car('Alto','Maruti','white')
print(c1.name)