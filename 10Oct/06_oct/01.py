##for i in range(1):
##    x=10
##
##if True:
##    y=4
##print(x,y)
##-

def fun():
##    global x
    x+=10

global x
x=20
fun()
print(x)
