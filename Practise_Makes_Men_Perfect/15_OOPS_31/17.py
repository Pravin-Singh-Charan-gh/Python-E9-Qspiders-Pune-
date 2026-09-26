# Exercise 17: Full-Time vs Part-Time Employee Pay Logic
# Problem Statement: Write a Python program that defines an Employee base class, then creates FullTimeEmployee and PartTimeEmployee subclasses, each implementing different pay calculation logic.

class Employee:
    def __init__(self,name):
        self.name = name
    def calculate_pay(self):
        return 0
    

class FullTimeEmployee(Employee):
    def __init__(self, name, annual_salary):
        super().__init__(name)
        self.annual_salary = annual_salary
    def calculate_pay(self):
        return self.annual_salary/12 

class PartTimeEmployee(Employee):
    def __init__(self,name, hourly_rates,hours_worked):
        super().__init__(name)
        self.hourly_rates = hourly_rates
        self.hours_worked = hours_worked

    def calculate_pay(self):
        return self.hourly_rates*self.hours_worked 

e1 = Employee('Mangilal')
fe1 = FullTimeEmployee('Chunnilal',1200000)
pe1 = PartTimeEmployee('Motilal',200,8)

print(e1.calculate_pay())
print(fe1.calculate_pay())
print(pe1.calculate_pay())