class Parent:
    a = 10
    b = 20

    def __init__(self,name,age):
        self.name = name
        self.age = age 

class Child(Parent):
    c = 30
    d = 40

p1 = Parent('Abhishek',50)
c1 = Child('Aradhya',15)
