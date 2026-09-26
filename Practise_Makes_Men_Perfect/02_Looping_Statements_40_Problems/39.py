# Exercise 39. flatten a nested list using loops
# Practice Problem: Given a nested list (a list containing other lists), write a program to “flatten” it into a single list containing all the individual elements.

nl = [[10, 20], [30, 40], [50, 60]]

fl = []

for l in nl:
    for i in l:
        fl.append(i)
print(fl)