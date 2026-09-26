class Person:
    def __init__(self,name, age=18):
        self.name= name
        self.age = age

    def print_details(self):
        print('Name :',self.name)
        print('Age :',self.age)

p1 = Person("Pravin",23)

# p1.name = "Pravin Singh"
# p1.age = 23

# print(p1.name)
# print(p1.age)

p1.print_details()