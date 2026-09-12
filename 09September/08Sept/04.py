#WAP to find the largest number in the list


lst = [1,2,3,4,5,67,121,89,34]

maxi = lst[0]
i = 1

while i < len(lst):
    if lst[i]>maxi:
        maxi=lst[i]
    i+=1
print(maxi)