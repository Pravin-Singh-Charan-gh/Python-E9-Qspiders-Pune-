

nl = eval(input('Enter the data : '))

for i in nl:
    if type(i)!=list:
        print(i)
    else:
        for j in i:
            print(j)
