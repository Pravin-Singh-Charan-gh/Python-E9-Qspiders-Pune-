# Exercise 10. Call Function using Positional and Keyword Arguments
# Practice Problem: Define a function describe_pet(animal_type, pet_name) that prints a description of a pet. Call this function twice: once using positional arguments and once using keyword arguments.

def describe_pet(animal_type,pet_name):
    print(animal_type,pet_name)

describe_pet('Dog','Sheru')
describe_pet(animal_type='Cow',pet_name='Payal')