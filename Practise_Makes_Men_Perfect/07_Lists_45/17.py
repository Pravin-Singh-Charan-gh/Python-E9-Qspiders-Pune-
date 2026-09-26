# Exercise 17. Count Occurrences of an Item
# Practice Problem: Find out how many times a specific value appears in a list.

nums = eval(input('Enter the list : '))
ele = int(input('Enter the element : '))

# ans = 0
# for i in nums:
#     if i==ele:
#         ans+=1

# using .count()
ans = nums.count(ele)
print(ans)