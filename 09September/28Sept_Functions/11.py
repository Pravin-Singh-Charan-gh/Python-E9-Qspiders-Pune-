#WAP to find the smallest number is a list

def smallest(l):
    mini = l[0]
    for i in l:
        mini = min(i,mini)
    return mini

l = eval(input('Enter the list : '))
print('Minimum Number:',smallest(l))