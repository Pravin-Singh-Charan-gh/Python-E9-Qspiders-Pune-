# Exercise 29. Find common elements (Intersection) using loop
# Practice Problem: Given two lists, find the elements that appear in both. Do not use Python’s built-in set().intersection() method.

l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]

ans = []
for i in l1:
    if i in l2:
        ans.append(i)
print(ans)

# 1.0