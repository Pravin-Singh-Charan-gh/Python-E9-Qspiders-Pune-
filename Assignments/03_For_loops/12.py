# 12. Remove duplicate elements from list (without using set).

nums = eval(input('Enter the list : '))

i = 0
while i<len(nums):
    if nums[i] in nums[:i]:
        nums.pop(i)
        i-=1
    i+=1

print(nums)