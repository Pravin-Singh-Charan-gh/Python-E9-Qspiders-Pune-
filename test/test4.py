class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

c1 = Car('Maruti Suzuki','e-vitara')

print(c1.model)

c1.model='Brezza'

del c1.model
print(c1.model)
