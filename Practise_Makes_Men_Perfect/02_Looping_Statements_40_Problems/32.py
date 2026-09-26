# Exercise 32. List Rotation: Rotate elements left by k positions
# Practice Problem: Given a list and an integer k, rotate the list to the left by k positions. For example, if k=2, the first two elements move to the end of the list.

l = [1,2,3,4,5]
k = 2

l = l[k:]+l[:k]

print(l)