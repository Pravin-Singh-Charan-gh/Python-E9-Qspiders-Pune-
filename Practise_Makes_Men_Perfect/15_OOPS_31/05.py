##Exercise 5: Product Class with Stock Value Calculator
##Problem Statement: Write a Python program to create a Product class with three instance attributes: name, price, and quantity. Add a method total_value() that returns the total stock value by multiplying price by quantity.

class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def total_value(self):
        return self.price*self.quantity

p1 = Product('biscuit',20,100000)
print(f"Total Value of {p1.name} is {p1.total_value()}")
