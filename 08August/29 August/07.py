#WAP to check whether the data is list then fetch the first value of list if it is integer or if data is tuple, then fetch the last value of tuple only if it is string

data = eval(input("Enter the data : "))

if type(data)==list and len(data)>0 and type(data[0])==int:
    print(data[0])

elif type(data)==tuple and len(data)>0 and type(data[-1])==str:
    print(data[-1])