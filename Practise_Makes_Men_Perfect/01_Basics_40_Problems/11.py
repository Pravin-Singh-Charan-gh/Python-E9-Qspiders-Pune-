#Write a script that takes a list containing duplicate items and returns a new list with only unique elements.

def remove_duplicate_from_list(lst):
    is_present=set()
    i = 0
    while i < len(lst):
        if lst[i] in is_present:
            lst.pop(i)
            i-=1
        is_present.add(lst[i])
        i+=1
        
nums = eval(input('Enter the list : '))
remove_duplicate_from_list(nums)
print(nums)

# using set then convert it back to list
nums = eval(input('Enter the list : '))
nums = list(set(nums))
print(nums)
