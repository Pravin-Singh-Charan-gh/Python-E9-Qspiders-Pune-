def fun():
    global x
    x+=10
    print('inside fun', id(x))

x=10
print('before fun',id(x))

fun()

print('after fun',id(x))