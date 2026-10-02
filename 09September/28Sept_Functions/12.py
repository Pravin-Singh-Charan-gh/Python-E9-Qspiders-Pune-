#WAP to find the second smallest number in a list

#WAP to find second largest number in a list

def sec_min(l):
    min1 = min2 = float('inf')

    for i in l:
        if i<min1:
            min1,min2 = i,min1
        elif i<min2 and i>min1:
            min2 = i

    return min2

l = eval(input('Enter the list : '))
print('Second Maximum :',sec_min(l))