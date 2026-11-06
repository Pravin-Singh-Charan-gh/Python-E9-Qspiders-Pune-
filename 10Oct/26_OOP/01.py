class BankAccount:
    def __init__(self,name,acc,bal,pin):
        self.name = name
        self.acc = acc
        self.bal = bal
        self.pin = pin

    def deposit(self,amount,pin):
        if amount>0 and pin==self.pin:
            self.bal += amount
            return 'Deposited to account'
        return False

class Loan:
    def __init__(self,p,i,t):
        self.p = p
        self.i = i
        self.t = t

    def installment(self,amount):
        pass        


class LoanAccount(BankAccount,Loan):
    def __init__(self,name,acc,bal,pin,p,i,t):
        super().__init__(name,acc,bal,pin)
        Loan.__init__(self,p,i,t)

    def installment(self,amount,pin):
         inst = self.calculate_installment()
         if inst == amount:
             self.deposit(amount,pin)
             return 'Amount Deposited Successfully'
         return f'Pay {inst}'

    def calculate_installment(self):
        interest = (self.p*self.i*self.t)/100
        total = self.p + interest
        return total//(self.t*12)

la1 = LoanAccount('Amit',12345,100000,123,100000,12,5)
print(la1.installment(2666,123))
