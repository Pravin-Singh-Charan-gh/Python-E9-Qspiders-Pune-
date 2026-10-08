#WAP to check if all the positional length arguments are integer or not

def is_int(*args):
    for i in args:
        if type(i)!=int:
            return False
    return True

print(is_int(1,2,3,4))
print(is_int(1,2,3,4,'abc'))
