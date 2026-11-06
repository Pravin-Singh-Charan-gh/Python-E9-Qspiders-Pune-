class CarRental:
    car_on_rent = ['ertiga','aura','omni','scorpio']
    rent = {}

    def __init__(self,name,dl,phone):
        self.name = name
        self.dl = dl
        self.phone =phone

    def rent_car(self,car_name):
        if car_name not in self.car_on_rent:
            return False,'Car not present'

        self.rent[self] = car_name
        self.car_on_rent.remove(car_name)
        return True, 'Car rented'

user = CarRental('Amit','huf7832',7242364253)
print(user.rent_car('omni'))