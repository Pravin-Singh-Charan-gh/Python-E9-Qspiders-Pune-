# Exercise 19: Media Subclasses with Type-Specific Attributes
# Problem Statement: Write a Python program that defines a Media base class, then creates Book, Magazine, and DVD subclasses, each with type-specific attributes and a describe() method.

class Media:
    def __init__(self,title,price):
        self.title = title
        self.price = price
    def describe(self):
        return f"{self.title} -Rs{self.price}"

class Book(Media):
    def __init__(self,title,price,author):
        super().__init__(title,price)
        self.author = author

    def describe(self):
        return f'Book: {self.title}, Author : {self.author}, Price : {self.price}.'
    
class Magazine(Media):
    def __init__(self,title,price,frequency):
        super().__init__(title,price)
        self.frequency = frequency
    def describe(self):
        return f'Magazine : {self.title}({self.frequency}), Price : {self.price}.'
    
class DVD(Media):
    def __init__(self,title,price,duration):
        super().__init__(title,price)
        self.duration = duration

    def describe(self):
        return f'DVD : {self.title},{self.duration} Mins, Price : {self.price}'

b1 = Book('Reach dad, Poor dad',300, 'Robert Kiyosaki and Sharon Lechter')
m1 = Magazine('XYZ',200, 'monthly')
d1 = DVD('DVD1',200,40)

print(b1.describe())
print(m1.describe())
print(d1.describe())