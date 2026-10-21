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
            return False,'Invalid Amount'
        self.bal+=amount
        return True,f'{amount} deposited succesfully \nAvailable Balance : {self.bal}'

    def withdraw(self,amount):
        if type(amount) not in (int,float):
            return False,'Only Numbers are allowed'
        if 0 < amount:
            if amount<self.bal:
                self.bal-=amount
                return True,f'{amount}Rs withdrawn successfully'
                
            else:
                return False,'Insufficient Fund'
        else:
            return False,'Amount cannot be negative'

    def transfer(self,other_account, amount): 
        if type(amount) not in (int,float):
            return False, "Amount should be number"
        if self.withdraw(amount)[0]:
            if other_account.deposit(amount)[0]:
                return True,'Transaction Successful'
            self.deposit(amount)
        return False,'Transaction Failed'
        
        


b1 = Bank(123456789,1000,1234)
b2 = Bank(3212312421,1200,9484)

print(b1.transfer(b2,1000))
