#WAP which takes 3 keyword only arguments and show them with
#argument name and value

##def fun(**kwargs):
##    if len(kwargs)>=3:
##        for i in kwargs:
##            print(i,':',kwargs[i])
##    else:
##        print('Length less than 3')

def fun(**kwargs):
    if len(kwargs)>=3:
        print(*kwargs.items(),sep='\n')
    else:
        print('Number of arguments are less than 3')

d1 = {'a':1,
     'b':2,
     'c':3}

d2 = {'b':2,
     'c':3}
fun(**d1)
fun(**d2)
