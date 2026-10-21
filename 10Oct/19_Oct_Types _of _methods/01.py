class Bank:
    def __init__(self,acc,bal,pin):
        self.acc= acc
        self.bal = bal 
        self.pin = pin 

    def show_details(self):
        print(f'Account : {self.acc}')
        print(f'Balance : {self.bal}')
 
    def deposit(self,amount):
        if amount<=0:
            print('Invalid Amount')
            return 
        self.bal+=amount
        print(f'{amount} deposited succesfully')
        print(f'Available Balance : {self.bal}')

    def withdraw(self,amount):
        if type(amount) not in (int,float):
            print('Only Numbers are allowed')
            return
        if 0 < amount:
            if amount<self.bal:
                self.bal-=amount
                print(f'{amount}Rs withdrawn successfully')
                return
            else:
                print('Insufficient Fund')
        else:
            print('Amount cannot be negative')
        


b1 = Bank(123456789,1000,1234)
b1.show_details()

b1.deposit(-4)
b1.deposit(20000)

b1.withdraw(50000)
b1.withdraw(5000)