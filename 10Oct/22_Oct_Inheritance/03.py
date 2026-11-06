class Bank:
    roi = 6

    def __init__(self,acc,bal):
        self.acc = acc
        self.bal = bal

    def bank_details(self):
        return f'''roi : {self.roi}
acc : {self.acc}
bal : {self.bal}'''

class SavingAccount(Bank):
    roi = 10

s1 = SavingAccount(123123123,10000000)
print(s1.bank_details())
