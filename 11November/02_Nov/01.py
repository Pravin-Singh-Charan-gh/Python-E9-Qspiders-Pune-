from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self,acc,bal,pin):
        self.acc = acc 
        self.bal = bal 
        self.pin = pin 

    @abstractmethod
    def deposit():
        pass

class Savings(BankAccount):
    def withdraw(self,amount):
        self.bal -= amount

    def deposit():
        pass 
                                
s1 = Savings(1234,1000,121)     
b1 = BankAccount(12345,100,11)