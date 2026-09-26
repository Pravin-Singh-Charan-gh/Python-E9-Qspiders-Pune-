##Exercise 26: Private Balance with Property Getter & Setter
##Problem Statement: Write a Python program that creates a BankAccount class where the balance is stored as a private attribute __balance, and exposed safely through a @property getter and a setter that validates the value before updating it.

class BankAccount:
    def __init__(self,balance):
        self._balance = balance
    
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self,amount):
        if amount<0:
            print('Invalid Balance.')
        else:
            self._balance = amount
    def deposit(self,amount):
        if amount<0:
            print('Invalid Amount.')
        else:
            self._balance += amount
            print(f'{amount} deposited successfully')

ac1 = BankAccount(10000)
print('Balance :',ac1.balance)

ac1.deposit(1000)
print('Balance :',ac1.balance)

ac1.balance -=100
print('Balance :',ac1.balance)
