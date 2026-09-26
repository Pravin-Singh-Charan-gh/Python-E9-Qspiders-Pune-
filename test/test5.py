class Person:
    last_name = 'Singh Charan'

    def __init__(self,first_name):
        self.first_name = first_name

    def show(self):
        print(f"{self.first_name} {self.last_name}")
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

p1 = Person('Pravin')
p2 = Person('Chhotu')
p1.show()
p2.show()

p2.last_name='Dan'
p1.last_name='Singh'
Person.last_name='Singh'
p1.show()
p2.show()

Person.age = 25
print(p1.age)
print(p2.age)

print(p1,p2)