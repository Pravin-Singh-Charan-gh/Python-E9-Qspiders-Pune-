""" Datatypes
name : string, price : integer, nutrients : dictionary (key : nutrient, value : percentage of that nutrient), ingredients :dictionary
(key : ingredient, value : )

"""

class Food:
    def __init__(self,name, price, nutrients, ingredients, stock):
        self.name = name
        self.price = price
        self.nutrients = nutrients
        self.ingredients = ingredients
        self.stock = stock

    def change_name(self,name):
        self.name = name

    def change_price(self,price):
        self.price = price 

