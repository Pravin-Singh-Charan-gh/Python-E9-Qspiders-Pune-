# Static Method

class CartoonNetwork:
    @staticmethod
    def welcome(name):
        return f'Welcome {name}, to the cartoon network'
    

print(CartoonNetwork.welcome('Prem'))

sinchan = CartoonNetwork()
print(sinchan.welcome('Sujal'))
