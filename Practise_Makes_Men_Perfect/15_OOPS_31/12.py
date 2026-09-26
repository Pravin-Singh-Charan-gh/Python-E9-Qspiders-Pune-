# Exercise 12: Shared Class Attribute Across Instances
# Problem Statement: Write a Python program to create a Vehicle class with a class attribute color = "White" that is shared by all instances. Create two vehicle objects and demonstrate that both share the same default color, then show that changing the class attribute updates all instances that have not overridden it.

class Vehicle:
    color = 'White'

v1 = Vehicle()
v2 = Vehicle()
print(f'v1 color : {v1.color}')
print(f'v2 color : {v2.color}')

v1.color='Magma Red'
print(f'v1 color : {v1.color}')
print(f'v2 color : {v2.color}')

