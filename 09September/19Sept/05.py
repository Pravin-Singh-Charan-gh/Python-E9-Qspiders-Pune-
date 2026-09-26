#Given a list of names print :
##1 name1
##2 name2
##3 name3

names = eval(input('Enter the list of names : '))

for i,j in enumerate(names,1):
    print(i,j)