##Exercise 26. Find the Second Largest Number in a List
##Practice Problem: Write a Python function that takes a list of numbers and returns the second largest value. Ensure the function handles lists with duplicate values correctly (e.g., if the list is [10, 10, 9], the second largest is 9).

def sec_max(l):
    lar =sec_lar= -float('inf')
    for i in l:
        if i>lar:
            lar,sec_lar = i,lar
        elif i>sec_lar and i!=lar:
            sec_lar = i
    return sec_lar

l = eval(input('Enter the list : '))
print(sec_max(l))