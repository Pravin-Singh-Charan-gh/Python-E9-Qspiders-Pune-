# Exercise 11. List Slicing: Extract Middle Elements
# Practice Problem: Given a list, extract a “slice” containing the middle three elements.

l = eval(input('Enter the list : '))
size = len(l)
print(l[size//2-1:size//2+2])