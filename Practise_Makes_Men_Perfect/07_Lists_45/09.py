# Exercise 9. Create a Copy of a List
# Practice Problem: Create a copy of an existing list so that modifying the copy does not change the original.

import copy

l = eval(input('Enter the list : '))

n_list = copy.deepcopy(l)

print(n_list)