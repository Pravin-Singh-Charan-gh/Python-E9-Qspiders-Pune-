##Exercise 6: Bank Account with Deposit & Overdraw Protection
##Problem Statement: Write a Python program to create a BankAccount class with a balance attribute and two methods: deposit(amount) that adds funds to the balance, and withdraw(amount) that deducts funds but prevents the balance from going below zero.

class BankAccount:
    def __init__(self,balance):
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"{amount}Rs deposited sussefully")
        print(f"Available Balance : {self.balance} Rs")



    def withdraw(self,amount):
        if amount>self.balance:
            print('Insufficient Balance :',self.balance)
        else:
            self.balance-=amount
            print(f"{amount} deducted sussefully")
            print(f"Available Balance : {self.balance}")

b1 = BankAccount(10000)
b1.deposit(5000)
b1.withdraw(2000000)
b1.withdraw(10000)
