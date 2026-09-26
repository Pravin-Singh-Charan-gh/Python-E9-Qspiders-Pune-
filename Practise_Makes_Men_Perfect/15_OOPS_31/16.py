# Exercise 16: Polymorphism with Dog & Cat speak()
# Problem Statement: Write a Python program that defines an Animal base class with a speak() method, then overrides it in Dog and Cat subclasses to return their respective sounds.

class Animal:
    def speak(self):
        print('Animal is Speaking')
class Dog(Animal):
    def speak(self):
        print('Woof!')
class Cat(Animal):
    def speak(self):
        print('Meow !')

a1 = Animal()
d1 = Dog()
c1 = Cat()

a1.speak()
d1.speak()
c1.speak()