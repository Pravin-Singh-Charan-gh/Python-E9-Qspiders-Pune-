# Exercise 11: Coffee Machine with Multi-Resource Tracking
# Problem Statement: Write a Python program to create a CoffeeMachine class that tracks three resource attributes: water, coffee, and milk (in ml/g). Add a make_latte() method that checks whether sufficient resources are available, deducts them if so, and prints an appropriate message in either case.

class CoffeeMachine:
    def __init__(self,water,coffee,milk):
        self.water = water
        self.coffee=coffee
        self.milk=milk
    def make_latte(self):
        if self.water<200:
            print(f'Insuffient Water : {self.water}ml')
        elif self.coffee<20:
            print(f'Insuffient Coffee : {self.coffee}gm')
        elif self.milk<150:
            print(f'Insuffient Milk : {self.milk}ml')
        else:
            print('Latte Ready to serve')

cm1 = CoffeeMachine(200,100,100)
cm1.make_latte()

cm1.milk+=100
cm1.make_latte()