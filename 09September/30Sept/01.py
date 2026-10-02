"""
Arguments : it is a input we give while calling the function.
Types of Argument
(i) Positional Argument
In this type of argument, the values are assigned to the parameter in the same order as they are passed as an argument
"""

# def add(a,b):
#     print(a)
#     print(b)
# add(10,20)

"""
(ii) Keyword Argument
In this argument, we pass the value of a parameter using paramter name
_> Keyword arguments can be passed in any order
"""
# def info(name,age,birthday):
#     print(f"""The name of the user is {name}. 
# age = {age},
# birthday = {birthday}""")

# info(name = "Pravin Singh", birthday='30/08/2003',age=23)

"""
=> Combination of Positional and Keyword Argument
Inorder to use combination of keyword and positional argument, keyword argument should come after the positional argument
"""
# def info(name,m_name,f_name, aunty, dob):
#     print(f''''name : {name}
# mother name : {m_name}
# father name : (f_name)
# aunty : {aunty}
# date of birth : {dob}''')

# info('Abhishek b', aunty='rekha', f_name='Amitabh B',m_name='jaya',dob='2-oct')  # WORKS
# info('Abhishek b', aunty='rekha', f_name='Amitabh B',m_name='jaya','2-oct')  #ERROR as dob is passed as positional arg which is passed after keyword arg
################################################3

# def demo(a,b,c,d):
#     print(a,b,c,d)

# demo(10,20,d=30,100) #ERROR
# demo(10,20,30,d=12,40)   #ERROR
# multiple value for argument a

# demo(10, b=20, c=30,d=40)


"""
(iii) Positional Only Arguments:
-> We can pass a slash parameter while declaring the function after all the parameters
-> This slash will make sure that all the parameter before it is positional only argument
"""

# def add(a,b,c,/):
#     print(a+b+c)
# add(a=10,b=20,c=30) #ERROR
# add() got some positional-only arguments passed as keyword arguments: 'a, b, c'

# add(10,20,30) #60
# We can add more arguments after slash which are keyword argument
def add(a,b,c,/,d,e):
    print(a+b+c+d+e)
add(1,2,3,4,e=5)

"""
(iv) Keyword Only Argument
We can pass asterisk (*) paramter to restrict all the parameter after asterisk from positional argument and can only be passed as an keyword argument.
 """
def info(*,name,age,dob):
    print(name,age,dob)
# info('Mohit','30','22-oct') #ERROR
# info() takes 0 positional arguments but 3 were given
info('Mohit',age='30',dob='22-oct')