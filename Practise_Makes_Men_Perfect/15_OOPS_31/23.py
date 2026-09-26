##Exercise 23: Type Checking with isinstance() & issubclass()
##Problem Statement: Write a Python program that uses isinstance() to check whether an object is an instance of a given class, and issubclass() to check whether one class is a subclass of another.

class Animal:
    pass
class Cow(Animal):
    pass

a1 = Animal()
c = Cow()

print('Is a1 a instance of Animal Class :', isinstance(a1,Animal))
print('Is c a instance of Animal Class :', isinstance(c,Animal))
print('Is Cow a subclass of Animal Class :', issubclass(Cow,Animal))
print('Is Animal a subclass of Cow Class :', issubclass(Animal,Cow))
print('Is Animal a subclass of Animal Class :', issubclass(Animal,Animal))
