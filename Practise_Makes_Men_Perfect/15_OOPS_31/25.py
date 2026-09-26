##Exercise 25: Cart Length Using len Overloading
##Problem Statement: Write a Python program that creates a Cart class that stores a list of items, and implements __len__ so that calling len(cart) returns the number of items currently in the cart.

class Cart:
    def __init__(self):
        self.items= []
        
    def add_item(self,item):
        self.items.append(item)
        
    def add_items(self,items):
        self.items.extend(items)
        
    def __len__(self):
        return len(self.items)

c1 = Cart()
c1.add_items(['biscuit','milk','sweet','bottle'])
print(f'Length of Cart : {len(c1)}')
