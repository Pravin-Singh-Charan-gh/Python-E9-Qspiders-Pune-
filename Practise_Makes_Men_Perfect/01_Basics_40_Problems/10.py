#Given a list of integers, find and print both the largest and the smallest numbers.

def maxInt_in_list(lst):
    ans = lst[0]
    for i in lst:
        if i>ans:
            ans=i
    return ans

def minInt_in_list(lst):
    ans = lst[0]
    for i in lst:
        if i<ans:
            ans= i
    return ans

lst = eval(input('Enter the list : '))
print('Maximum value : ',maxInt_in_list(lst))
print('Minimum value : ',minInt_in_list(lst))

print('Using inbuilt functions : ')
print('Maximum value : ',max(lst))
print('Minimum value : ',min(lst))
