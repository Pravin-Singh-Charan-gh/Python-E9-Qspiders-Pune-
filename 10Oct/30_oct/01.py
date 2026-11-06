class BankAccount:
    def __init__(self,acc,bal,pin):
        self.acc = acc 
        self._bal = bal 
        self.__pin = pin 

    def getPin(self):
        return self.__pin

    def setPin(self,pin):
        self.__pin = pin

obj = BankAccount(1234,10000,1111)
print(obj.acc)
print(obj._bal)
# print(obj.__pin)

obj._BankAccount__pin = 22222
print(obj.getPin())
help()