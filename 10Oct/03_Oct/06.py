#WAF to which takes n number of keyword argument and check if the number of argument
#is greater than 10 or not

def fun(a,b,c,s1,s2,**kwargs):
    if not (type(a)==type(b)==type(c)==int):
        return 'First 3 Arguments should be number.'
    if not(type(s1)==type(s2)==str):
        return 'First name and Last name should be string.'
    if len(kwargs)<=5:
        return 'Give atleast 5 keyword arguments'
    return 'ALL ARE VALID'

print(fun(1,2,3,'a','b',x=3,y=4,z=6,a=2,b=9))
