#Write a function to return True if the first and last number of a given list is the same. If the numbers are different, return False.

def is_same(nums):
    return nums[0]==nums[-1]

nums = eval(input('Enter the list : '))

if is_same(nums):
    print('First and last number of list is same')
else:
    print('First and last number of list is not same')
    
