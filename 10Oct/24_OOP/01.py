class BankAccount:
    def __init__(self,acc,bal):
        self.acc = acc
        self.bal = bal

    def deposit(self,amount):
        if amount <= 0:
            return False,'Amount cannot be negative'
        self.bal += amount
        return True,'Amount Deposited Succesfully'

class SavingAccount(BankAccount):
    def deposit(self,amount):
        if 10000>=amount>=500:
            return super().deposit(amount)
        return False,'Amount should be between 500 and 10000'

obj = SavingAccount(12345,200)
print(obj.deposit(2000))
