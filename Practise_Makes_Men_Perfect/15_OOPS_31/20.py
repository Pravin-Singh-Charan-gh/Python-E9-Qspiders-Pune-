# Exercise 20: Discounted Order Subclass with 10% Off
# Problem Statement: Write a Python program that creates an Order class with a total amount, then creates a DiscountedOrder subclass that applies a 10% discount to the total.

class Order:
    def __init__(self,order_id, total):
        self.order_id = order_id
        self.total = total
    def get_total(self):
        return self.total

class DiscountedOrder(Order):
    def __init__(self, order_id,total):
        super().__init__(order_id,total)
    def get_total(self):
        return self.total-self.total*0.1
    
o1 = Order(101,100)
do1 = DiscountedOrder(102,100)
print('Order total :',o1.get_total())
print('Discounted Order total',do1.get_total())