##Exercise 4: Student Class with Average Grade
##Problem Statement: Write a Python program to create a Student class that stores a student’s name and a list of marks. Add a method average() that calculates and returns the average of all marks.

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def average(self):
        return sum(self.marks)/len(self.marks)

s1 = Student('Pravin',[100,98,97,99,100,98])
print(s1.average())
