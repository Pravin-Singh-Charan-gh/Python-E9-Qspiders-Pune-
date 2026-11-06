class Data:
    def __init__(self,data):
        self.data = data

    def __add__(self,other):
        return self.data + other.data

    def __mul__(self,other):
        return self.data * other.data

    def __mod__(self,other):
        return self.data  % other.data

    def __gt__(self,other):
        return self.data>other.data
    
    def __ge__(self,other):
        return self.data >= other.data

d1 = Data(10)
d2 = Data(20)
