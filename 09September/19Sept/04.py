#WAP to find the index of given element from a list

l = eval(input('Enter the list : '))
k = int(input('Enter the value to find index of : '))

##en_l = enumerate(l)

for i in range(len(l)):
    if l[i]==k:
        print(i)
        break

for i,j in enumerate(l):
    if j == k:
        print(i)
