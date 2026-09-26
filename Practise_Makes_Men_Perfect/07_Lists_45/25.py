# Exercise 25. Replace List’s Item with New Value if Found
# Practice Problem: Find the first occurrence of a specific value in a list and replace it with a new value.

nums = eval(input('Enter the list : '))
find = int(input('Enter the number to replace : '))
replace_with = int(input('Enter the number to replace with: '))

index = nums.index(find)
nums[index] = replace_with
print(nums)