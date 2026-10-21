#WAP to create a simple restaurent management system
##user-> see menu -> order item


class Restaurent:
    def __init__(self,name=''):
        self.name = name
        self.menu = []

    def add_item(self,item,price):
        self.menu.append((item,price))

    def display_menu(self):
        print(self.name)
        print('==========FOOD MENU==========')
        for food in self.menu:
            print(f'{food[0]} : {food[1]} Rs')
        print()

    def order_food(self,hotel,food):
        for item in hotel.menu:
            if item[0]==food:
                return True,f'{food} Ordered Successfully'
        return False,'Food Not Available'

##class Customer:
##    def __init__(self,name,phone):
##        self.name  =   name
##        self.phone = phone
##        self.hotel = 
##
##    def order_food(self,food_name):
        


r1 = Restaurent('Balaji Hotel')
r1.add_item('Jalebi',234)
r1.add_item('Rasgulla',234)
r1.add_item('Dal Bati',123)
r1.add_item('Sweets',343)
r1.add_item('Ras Malai',150)
r1.add_item('Aam Ras',122)

cust1 = Restaurent()
r1.display_menu()
print(cust1.order_food(r1,'Jalebi'))
