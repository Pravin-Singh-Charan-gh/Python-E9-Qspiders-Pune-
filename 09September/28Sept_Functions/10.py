#WAP to find second largest number in a list

def sec_max(l):
    max1 = max2 = -float('inf')

    for i in l:
        if i>max1:
            max1,max2 = i,max1
        elif i>max2 and i<max1:
            max2 = i

    return max2

# def sec_max(l):
    
#     max1 = max2 = 

#     for i in l:
#         if i>max1:
#             max1,max2 = i,max1
#         elif i>max2 and i<max1:
#             max2 = i

#     return max2
l = eval(input('Enter the list : '))
print('Second Maximum :',sec_max(l))