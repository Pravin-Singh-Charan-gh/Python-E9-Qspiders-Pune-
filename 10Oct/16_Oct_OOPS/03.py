#WAP to create a Bank class with a  constructor which creates a username,
#account number and bank balance


class Account:
    def __init__(self,username,account_number, balance):
        self.username = username
        self.account_number = account_number
        self.balance = balance

b1 = Account('Amit',123123871236,100000)

