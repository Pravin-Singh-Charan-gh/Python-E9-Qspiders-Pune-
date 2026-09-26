#Iterate through a given list of numbers and print only those numbers which are divisible by 5.

def div_by_5(nums):
    for i in nums:
        if i%5==0:
            print(i,end=', ')

nums = eval(input('Enter the list : '))
div_by_5(nums)
