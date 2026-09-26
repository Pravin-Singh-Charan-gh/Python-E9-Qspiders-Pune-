# Exercise 18. Remove All Occurrences of a Specific Item
# Practice Problem: Delete every instance of a specific value from a list.

nums = eval(input('Enter the list : '))
ele = int(input('Enter the number to delete : '))

ans = [num for num in nums if num!=ele]
print(ans)