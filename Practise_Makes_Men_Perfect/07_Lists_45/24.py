# Exercise 24. Add New Item After a Specified Item
# Practice Problem: Find a specific item in a list and insert a new item immediately after it.

nums = eval(input('Enter the list : '))
insert_after = int(input('Enter the number to insert after : '))
to_insert = int(input('Enter the number to insert : '))

index = nums.index(insert_after)+1
nums.insert(index,to_insert)

print(nums)