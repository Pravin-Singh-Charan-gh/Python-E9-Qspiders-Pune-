class Parent:
    a = 10
    b = 20

    def __init__(self,name,age):
        self.name = name
        self.age = age 

class Child(Parent):
    c = 30
    d = 40

    def __init__(self,dob,gender):
        self.dob = dob
        self.gender = gender

p1 = Parent('Abhishek',50)
##c1 = Child('Aradhya',15,'30-August','male')

c2 = Child('30-August','male')
