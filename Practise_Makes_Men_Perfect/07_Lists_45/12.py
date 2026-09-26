# Exercise 12. Swap Two Elements at Given Indices
# Practice Problem: Write a script to swap the positions of two elements in a list based on their indices.

l = eval(input('Enter the list : '))
i1 = int(input('Enter the first index : '))
i2 = int(input('Enter the second index : '))

l[i1],l[i2] = l[i2],l[i1]

print(l)