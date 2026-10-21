class Cafe:
    menu = {
        'pizza':['sweetcorn pizza','paneer tikka'],
        'burger' : ['classic burger','veg crispy burger'],
        'coffee':['coffee','cold coffee']

    def __int__(self):
        self.cart = []

    def add_to_cart(self, opt, sub_opt):
        if self.menu.get(opt):
            if 0<=sub.opt <len(self.menu[opt]):
                self.cart += [self.menu[opt] [sub_opt]]
