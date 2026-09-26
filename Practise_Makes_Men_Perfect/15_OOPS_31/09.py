# Exercise 9: Temperature Class with Unit Converters
# Problem Statement: Write a Python program to create a Temperature class that stores a temperature in Celsius. Add two methods: to_fahrenheit() that converts and returns the value in Fahrenheit, and to_kelvin() that converts and returns the value in Kelvin.

class Temperature:
    def __init__(self,celsius):
        self.celsius = celsius
    def to_fahrenhit(self):
        return (self.celsius*9/5)+32

    def to_kelvin(self):
        return self.celsius + 273.15

temp = Temperature(25)
print("Celsius :",temp.celsius)
print("Fahrenhite :",temp.to_fahrenhit())
print("Kenvin :",temp.to_kelvin())