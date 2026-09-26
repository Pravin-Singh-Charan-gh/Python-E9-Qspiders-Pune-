# Exercise 10. Combine Two Lists
# Practice Problem: Merge two separate lists into a single, unified list.

l1 = eval(input('Enter the first list : '))
l2 = eval(input('Enter the second list : '))

l1.extend(l2)

print(l1)