# Exercise 20. Remove Duplicates from List
# Practice Problem: Remove all duplicate values from a list while keeping only one instance of each element.

nums = eval(input('Enter the list : '))

u_l = dict.fromkeys(nums)

print(f"Unique List: {u_l}")