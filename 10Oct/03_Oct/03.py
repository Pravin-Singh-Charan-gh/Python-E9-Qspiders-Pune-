#WAP to which takes keyword argument from the user and verify
#whether they have given name, number or email or not

##def verify(**kwargs):
##    return bool(kwargs.get('name') and kwargs.get('number') and kwargs.get('email'))

def verify(**kwargs):
    name = kwargs.get('name')
    number = kwargs.get('number')
    email = kwargs.get('email')

    if not name :
        return 'Name doesn\'t exist'
    elif not number :
        return 'Number doesn\'t exist'
    elif not email:
        return 'Email doesn\'t exist'
    return "VALID"

print(verify(name='Pravin',number = 11242344234,email='abc@gmail.com'))
